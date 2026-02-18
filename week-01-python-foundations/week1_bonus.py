# Soru 1: 0dan 29a kadar olan tek sayıların karesini içeren bir liste oluşturun.

list1 =[]
for i in range (30):
    if i % 2 != 0:
        list1.append(i ** 2)
print(list1)

list1_comp = [i ** 2 for i in range(30) if i % 2 != 0]
print(list1_comp)


# Soru 2: 10 ile 50 arasında 5'e tam bölünen sayıların listesini oluşturun.

list5 = list(range(15, 50 , 5))
print(list5)

list5_new = []
for i in range(11, 50):
    if i % 5 == 0:
        list5_new.append(i)
print(list5_new)

list5_comp = [i for i in range(11, 50) if i % 5 == 0]
print(list5_comp)


# Soru 3: Verilen bir sayı listesinde negatif olanları 0 ile değiştirerek yeni bir liste oluşturun.
ornek_liste = [-3, 4, -1, 6, 0]
ornek_liste2 =[]
for i in ornek_liste:
    if i < 0:
        ornek_liste2.append(0)
    else:
        ornek_liste2.append(i)
print(ornek_liste2)

ornek_liste_comp = [0 if i<0 else i for i in ornek_liste]
print(ornek_liste_comp)
# Soru 4: 1 ile 10 arasındaki bir sayı listesindeki tüm çift sayıları "çift", tek sayıları "tek" kelimesi ile değiştirin.
list_tc = []
for i in range(2, 10):
    if i % 2 == 0:
        list_tc.append("çift")
    else:
        list_tc.append("tek")
print(list_tc)

list_tc_comp = ["çift" if i % 2 ==0 else "tek" for i in range(2,10)]
print(list_tc_comp)
##Sadece sesli harfleri küçük harfle alıp bir liste oluştur. Tekrar eden harfleri alma.
metin = "Python DAtA Science BootcAmp"
sesli = "aeiouAEIOU"
list_harf = []
for i in metin:
    if i in sesli:
        list_harf.append(i.lower())

    if i in list_harf:
        list_harf.remove(i)


list_harf_comp = [{i.lower() for i in metin if i in sesli}]
print(list_harf_comp)

##İlk harfi 'a' veya 'e' olan isimleri büyük harfe çevirerek yeni bir liste oluştur.
isimler = ["mustafa", "ayşe", "mehmet", "Eda", "ali"]
new_isimler = []
for i in isimler:
    if i[0] in ["A", "a", "E", "e"]:
        new_isimler.append(i.upper())
print(new_isimler)

new_isimler_comp = [i.upper() for i in isimler if i[0] in ["A", "a", "E", "e"]]
print(new_isimler_comp)

##Kelime uzunluğu çift olanlara "MEYVE_", tek olanlara "TROPİK_" ön eki ekle.
urunler = ["elma", "muz", "kiraz", "kivi", "mandalina"]
new_urunler = []
for i in urunler:
    if len(i) % 2 != 0:
        new_urunler.append(f"TROPİK {i}")
    else:
        new_urunler.append(f"MEYVE {i}")


new_urunler_comp = [f"TROPİK {i}" if len(i) % 2 !=0 else f"MEYVE {i}" for i in urunler]

# Soru 5 BONUS: 0-99 arasındaki tüm asal sayıları içeren bir list comprehension yazınız.
# ilkel yöntem - for ile yaz
asal = []
for i in range(2, 100):
    for j in range (2, i):
        if i % j == 0:
            break
        else:
            asal.append(i)
print(asal)

asal_sayilar = []
for i in range(2, 100):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        asal_sayilar.append(i)
print(asal_sayilar)
# comprehension yöntemi 1

asal_comp = [i for i in range(2, 100) if all(i % j != 0 for j in range(2, i))]
print(asal_comp)


# comprehension yöntemi 2  - fonksiyon kullanarak yaz
def asalSayi(i):
    for num in range (2, i):
        if i%num == 0:
            print(f"{i} bir asal sayı değildir!")
            break
    else:
        print(f"{i} bir asal sayıdır!")

asalSayi(5)
asalSayi(6)



# Soru 6 BONUS: Aşağıdaki matrisin sadece köşegenindeki (i == j) elemanlarını alın.
matris = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]



for idx, row in enumerate(matris):
    print(row[idx])

new_matris = [row[idx] for idx, row in enumerate(matris)]
print(new_matris)
