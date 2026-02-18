
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from hypothesis.extra.pandas import columns

pd.set_option("display.max_columns", 500)
pd.set_option("display.max_rows", 500)


##############
## GÖREV 1 ##
##############
#Soru 1: persona.csv dosyasını okutunuz ve veri seti ile ilgili genel bilgileri gösteriniz.

df = pd.read_csv("databases/persona.csv")
df.info()
df.shape
df.describe()
df.head(10)
df.tail(10)
df.isnull().sum()
df.isnull().values.any()
df.columns
df.index

#Soru 2: Kaç unique SOURCE vardır? Frekansları nedir?

df["SOURCE"].nunique()
df["SOURCE"].unique()

#Soru 3: Kaç unique PRICE vardır?

df["PRICE"].nunique()
df["PRICE"].unique()

#Soru 4: Hangi PRICE'dan kaçar tane satış gerçekleşmiş?

df["PRICE"].value_counts()

#Soru 5: Hangi ülkeden kaçar tane satış olmuş?

df["COUNTRY"].value_counts()

#Soru 6: Ülkelere göre satışlardan toplam ne kadar kazanılmış?

df.groupby("COUNTRY")["PRICE"].sum()

#Soru 7: SOURCE türlerine göre satış sayıları nedir?

df["SOURCE"].value_counts()

#Soru 8: Ülkelere göre PRICE ortalamaları nedir?

df.groupby("COUNTRY")["PRICE"].mean()
df.groupby("COUNTRY").agg({"PRICE": "mean"})

#Soru 9: SOURCE'lara göre PRICE ortalamaları nedir?

df.groupby("SOURCE").agg({"PRICE": "mean"})

#Soru 10: COUNTRY-SOURCE kırılımında PRICE ortalamaları nedir?

df.groupby(["SOURCE", "COUNTRY"]).agg({"PRICE": "mean"})
df.pivot_table(values="PRICE", index="SOURCE", columns="COUNTRY")

####################################################################################
## GÖREV 2: COUNTRY, SOURCE, SEX, AGE kırılımında ortalama kazançlar nedir?##
####################################################################################

df.groupby(["COUNTRY", "SOURCE", "SEX", "AGE"]).agg({"PRICE": "mean"})
df.pivot_table("PRICE", index= ["COUNTRY", "SOURCE", "SEX", "AGE"])

####################################################################################
## GÖREV 3: Çıktıyı PRICE’a göre sıralayınız.
# Önceki sorudaki çıktıyı daha iyi görebilmek için sort_values metodunu azalan olacak şekilde PRICE’a göre uygulayınız.
# Çıktıyı agg_df olarak kaydediniz ##
####################################################################################

agg_df = df.groupby(["COUNTRY", "SOURCE", "SEX", "AGE"]).agg({"PRICE": "mean"}).sort_values(by= "PRICE", ascending = False)

####################################################################################
## GÖREV 4: Indekste yer alan isimleri değişken ismine çeviriniz.
# Üçüncü sorunun çıktısında yer alan PRICE dışındaki tüm değişkenler index isimleridir. Bu isimleri değişken isimlerine çeviriniz.
####################################################################################

agg_df.index
agg_df.reset_index(inplace= True)

####################################################################################
## GÖREV 5: Age değişkenini kategorik değişkene çeviriniz ve agg_df’e ekleyiniz.
# Age sayısal değişkenini kategorik değişkene çeviriniz.
# Aralıkları ikna edici şekilde oluşturunuz.
# Örneğin: ‘0_18', ‘19_23', '24_30', '31_40', '41_70'
####################################################################################

agg_df["CAT_AGE"] = pd.cut(agg_df["AGE"], [0, 18, 25, 35, 45, 70])
agg_df.head()
agg_df.info()
agg_df.columns

####################################################################################
## GÖREV 6: Yeni seviye tabanlı müşterileri (persona) tanımlayınız.
# Yeni seviye tabanlı müşterileri (persona) tanımlayınız ve veri setine değişken olarak ekleyiniz.
# Yeni eklenecek değişkenin adı: customers_level_based
# Önceki soruda elde edeceğiniz çıktıdaki gözlemleri bir araya getirerek customers_level_based değişkenini oluşturmanız gerekmektedir.
####################################################################################
agg_df["customers_level_based"] = [f"{v.values[0]}_{v.values[1]}_{v.values[2]}_{v.values[5].left + 1}_{v.values[5].right}" for index , v in agg_df.iterrows()]
agg_df.shape
agg_df = agg_df.groupby("customers_level_based").agg({"PRICE": "mean"})

####################################################################################
## GÖREV 7: Yeni müşterileri (personaları) segmentlere ayırınız.
# Yeni müşterileri (Örnek: USA_ANDROID_MALE_0_18) PRICE’a göre 4 segmente ayırınız.
# Segmentleri SEGMENT isimlendirmesi ile değişken olarak agg_df’e ekleyiniz.
# Segmentleri betimleyiniz (Segmentlere göre group by yapıp price mean, max, sum’larını alınız).
####################################################################################

agg_df["SEGMENT"] = pd.qcut(agg_df["PRICE"], 4, labels=["D", "C", "B", "A"])
agg_df.groupby("SEGMENT").agg({"PRICE": ["mean", "max", "sum"]})


####################################################################################
## GÖREV 8: Yeni gelen müşterileri sınıflandırıp, ne kadar gelir getirebileceklerini tahmin ediniz.
# 33 yaşında ANDROID kullanan bir Türk kadını hangi segmente aittir ve ortalama ne kadar gelir kazandırması beklenir?
# 35 yaşında IOS kullanan bir Fransız kadını hangi segmente aittir ve ortalama ne kadar gelir kazandırması beklenir?
####################################################################################

agg_df.reset_index(inplace= True)
agg_df.columns
new_user = "tur_android_female_26_35"
new_user2 = "fra_ios_female_26_35"
agg_df[agg_df["customers_level_based"] == new_user]
agg_df[agg_df["customers_level_based"] == new_user2]
agg_df[agg_df["SEGMENT"] == "A"]
agg_df.head(10)
