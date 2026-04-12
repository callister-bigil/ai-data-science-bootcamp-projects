SELECT * FROM "Customers"

-- 2. Kaç farklı müşterinin alışveriş yaptığını gösterecek sorguyu yazınız.
SELECT COUNT(DISTINCT("master_id")) FROM "Customers"

-- 3. Toplam yapılan alışveriş sayısı ve ciroyu getirecek sorguyu yazınız.
SELECT COUNT(master_id) AS TOTAL_SALE, (SUM(customer_value_total_ever_offline) + SUM(customer_value_total_ever_online)) AS CIRO FROM "Customers"

-- 4. Alışveriş başına ortalama ciroyu getirecek sorguyu yazınız.
SELECT (SUM(customer_value_total_ever_offline) + SUM(customer_value_total_ever_online))/COUNT(master_id) AS AVERAGE_CIRO FROM "Customers"

-- 5. En son alışveriş yapılan kanal (last_order_channel) üzerinden yapılan
-- alışverişlerin toplam ciro ve alışveriş sayılarını getirecek sorguyu yazınız.
SELECT 
	last_order_channel,
	(SUM(customer_value_total_ever_offline) + SUM(customer_value_total_ever_online)) AS CIRO,
	COUNT(master_id) AS TOTAL_SALE
FROM "Customers"
GROUP BY last_order_channel

-- 6. Store type kırılımında elde edilen toplam ciroyu getiren sorguyu yazınız.
SELECT 
	store_type,
	ROUND((SUM(customer_value_total_ever_offline) + SUM(customer_value_total_ever_online))) AS CIRO
FROM "Customers"
GROUP BY store_type

-- 7. Yıl kırılımında alışveriş sayılarını getirecek sorguyu yazınız (Yıl olarak
-- müşterinin ilk alışveriş tarihi (first_order_date) yılını baz alınız)
SELECT
    CASE
        WHEN EXTRACT(YEAR FROM AGE(first_order_date)) >= 7 THEN '7_year_and_greater'
        ELSE 'Less_then_7_year'
    END AS year_breakdown,
    COUNT(master_id) customer_number
FROM "Customers"
GROUP BY
    CASE
        WHEN EXTRACT(YEAR FROM AGE(first_order_date)) >= 7 THEN '7_year_and_greater'
        ELSE 'Less_then_7_year'
    END
ORDER BY year_breakdown;

-- 8. En son alışveriş yapılan kanal kırılımında alışveriş başına ortalama ciroyu
-- hesaplayacak sorguyu yazınız.
SELECT last_order_channel, AVG((customer_value_total_ever_offline)+(customer_value_total_ever_online))
FROM "Customers"
GROUP BY last_order_channel

-- 9. Son 12 ayda en çok ilgi gören kategoriyi getiren sorguyu yazınız.
SELECT
    TRIM(category) AS categories,
	COUNT(*) AS COUNTS
FROM "Customers",
LATERAL unnest(
    STRING_TO_ARRAY(
        REPLACE(REPLACE(interested_in_categories_12, '[', ''), ']', ''),
        ','
    )
) AS category
WHERE last_order_date >= (
    SELECT MAX(last_order_date) - INTERVAL '12 months'
    FROM "Customers"
)
GROUP BY TRIM(category)
ORDER BY COUNTS DESC
LIMIT 1;

-- 10. En çok tercih edilen store_type bilgisini getiren sorguyu yazınız.
SELECT store_type
FROM "Customers"
GROUP BY store_type
ORDER BY COUNT(master_id) DESC
LIMIT 1;

-- 11. En son alışveriş yapılan kanal (last_order_channel) bazında, en çok ilgi
-- gören kategoriyi ve bu kategoriden ne kadarlık alışveriş yapıldığını getiren
-- sorguyu yazınız.
SELECT last_order_channel, TRIM(category), COUNT(TRIM(category))
FROM "Customers",
LATERAL unnest(
    STRING_TO_ARRAY(
        REPLACE(REPLACE(interested_in_categories_12, '[', ''), ']', ''),
        ','
    )
) AS category
GROUP BY last_order_channel, TRIM(category)
ORDER BY COUNT(TRIM(category)) DESC;

SELECT channel, categories, counts
FROM (
	SELECT 
		channel,
		categories,
		counts,
		ROW_NUMBER() OVER (
			PARTITION BY channel
			ORDER BY counts DESC
		) AS ranks
	FROM (
		SELECT
			last_order_channel AS channel,
			TRIM(category) AS categories,
			COUNT(TRIM(category)) AS counts
		FROM "Customers",
		LATERAL unnest(
    		STRING_TO_ARRAY(
        		REPLACE(REPLACE(interested_in_categories_12, '[', ''), ']', ''),
        		','
			)
		) AS category
		GROUP BY last_order_channel, TRIM(category)
	) t
) x
WHERE ranks = 1;

-- 12. En çok alışveriş yapan kişinin ID’ sini getiren sorguyu yazınız.
SELECT master_id
FROM "Customers"
GROUP BY master_id
ORDER BY SUM(customer_value_total_ever_offline) + SUM(customer_value_total_ever_online) DESC
LIMIT 1

-- 13. En çok alışveriş yapan kişinin alışveriş başına ortalama cirosunu ve alışveriş
-- yapma gün ortalamasını (alışveriş sıklığını) getiren sorguyu yazınız.
SELECT AVG(customer_value_total_ever_offline + customer_value_total_ever_online)
FROM "Customers"
GROUP BY master_id
ORDER BY SUM(customer_value_total_ever_offline) + SUM(customer_value_total_ever_online) DESC
LIMIT 1

-- 14. En çok alışveriş yapan (ciro bazında) ilk 100 kişinin alışveriş yapma gün
-- ortalamasını (alışveriş sıklığını) getiren sorguyu yazınız.
SELECT (last_order_date::date - first_order_date::date)/(order_num_total_ever_online + order_num_total_ever_offline) AS buy_frequency
FROM "Customers"
ORDER BY (SELECT SUM(customer_value_total_ever_offline) + SUM(customer_value_total_ever_online) FROM "Customers") DESC
LIMIT 100;


-- 15. En son alışveriş yapılan kanal (last_order_channel) kırılımında en çok
-- alışveriş yapan müşteriyi getiren sorguyu yazınız.--------------------------------------------
SELECT channel, master_id, counts
FROM (
	SELECT 
		channel,
		master_id,
		counts,
		ROW_NUMBER() OVER (
			PARTITION BY channel
			ORDER BY counts DESC
		) AS ranks
	FROM (
		SELECT
			last_order_channel AS channel,
			master_id,
			order_num_total_ever_online + order_num_total_ever_offline AS counts
		FROM "Customers"
	) x
) t
WHERE ranks=1

-- 16. En son alışveriş yapan kişinin ID’ sini getiren sorguyu yazınız. (Max son
-- tarihte birden fazla alışveriş yapan ID bulunmakta. Bunları da getiriniz.)--------------------
SELECT *
FROM "Customers"
WHERE last_order_date = (SELECT MAX(last_order_date) FROM "Customers");

