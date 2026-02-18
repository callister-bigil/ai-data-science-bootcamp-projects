###############################################
# Python Alıştırmalar
###############################################

###############################################
# GÖREV 1: Veri yapılarının tipleriniz inceleyiniz.
###############################################

x = 8
type(x)

y = 3.2
type(y)

z = 8j +18
type(z)

a = "Hello World"
type(a)

b = True
type(b)

c = 23 < 22
type(c)

l = [1, 2, 3, 4]
type(l)

d = {"Name": "Jake",
     "Age": 27,
     "Address": "Downtown"}
type(d)

t = ("Machine Learning", "Data Science")
type(t)

s = {"Python", "Machine Learning", "Data Science"}
type(s)

###############################################
# GÖREV 2: Verilen string ifadenin tüm harflerini büyük harfe çeviriniz. Virgül ve nokta yerine space koyunuz, kelime kelime ayırınız.
###############################################

text = "The goal is to turn data into information, and information into insight."

Text = text.upper()
Text = Text.replace(".", " ")
Text = Text.replace(",", " ")
Text = Text.split()
print(Text)

###############################################
# GÖREV 3: Verilen liste için aşağıdaki görevleri yapınız.
###############################################

lst = ["D", "A", "T", "A", "S", "C", "I", "E", "N", "C", "E"]
len(lst)
lst[0]
lst[10]
lst[0:4]
lst.pop(8)
lst.append("B")
lst.insert(8, "N")
print(lst)

###############################################
# GÖREV 4: Verilen sözlük yapısına aşağıdaki adımları uygulayınız.
###############################################


dict = {"Christian": ["America", 18],
        "Daisy": ["England", 12],
        "Antonio": ["Spain", 22],
        "Dante": ["Italy", 25]}
dict.keys()
dict.values()
dict["Daisy"] = ["England", 13]
dict.update({"Daisy": ["England", 13]})
dict.update({"Ahmet": ["Turkey", 24]})
dict.pop("Antonio")

###############################################
# GÖREV 5: Arguman olarak bir liste alan, listenin içerisindeki tek ve çift sayıları ayrı listelere atıyan ve bu listeleri return eden fonskiyon yazınız.
###############################################

numbers = list(range(1, 11))

def tekciftayır(numbers):
    listtek = []
    listcift = []
    for number in numbers:
         if number % 2 == 0:
              listcift.append(number)
         else:
              listtek.append(number)
    print(listtek)
    print(listcift)

tekciftayır(list(range(5, 18)))

l = [2, 13, 18, 93, 22]


def odd_and_even(lst: list) -> tuple:
    """
    Docstring for odd_and_even

    :param lst: Description
    :type lst: list
    :return: Description
    :rtype: tuple
    """
    evens = list(filter(lambda x: x % 2 != 0, lst))
    odds = list(filter(lambda x: x % 2 == 0, lst))
    return evens, odds


e, o = odd_and_even(l)
print(e, o)

###############################################
# GÖREV 6: Aşağıda verilen listede mühendislik ve tıp fakülterinde dereceye giren öğrencilerin isimleri bulunmaktadır.
# Sırasıyla ilk üç öğrenci mühendislik fakültesinin başarı sırasını temsil ederken son üç öğrenci de tıp fakültesi öğrenci sırasına aittir.
# Enumarate kullanarak öğrenci derecelerini fakülte özelinde yazdırınız.
###############################################

ogrenciler = ["Ali","Veli","Ayşe","Talat","Zeynep","Ece"]


for index, ogrenci in enumerate(ogrenciler, 1):
     if index < 4:
          #print("Mühendislik Fakültesi " + str(index) + " . " + "öğrenci: " + str(ogrenci))
         print("Mühendislik Fakültesi", index, ".", "öğrenci:", ogrenci)
     else:
         # print("Tıp Fakültesi {} . öğrenci: {}".format(index - 3, ogrenci))
          print("Tıp Fakültesi", index - 3, ".", "öğrenci:", ogrenci)


###############################################
# GÖREV 7: Aşağıda 3 adet liste verilmiştir. Listelerde sırası ile bir dersin kodu, kredisi ve kontenjan bilgileri yer almaktadır. Zip kullanarak ders bilgilerini bastırınız.
###############################################

ders_kodu = ["CMP1005","PSY1001","HUK1005","SEN2204"]
kredi = [3,4,2,4]
kontenjan = [30,75,150,25]
for k,d,l in zip(kredi, ders_kodu, kontenjan):
    print("Kredisi", k, "olan", d , "kodlu dersin kontenjanı", l, "kişidir.")


#ziplist = list(zip(kredi, ders_kodu, kontenjan))
#print("Kredisi", ziplist[0][0], "olan", ziplist[0][1] , "kodlu dersin kontenjanı", ziplist[0][2],
#      "kişidir.\nKredisi", ziplist[1][0], "olan", ziplist[1][1] , "kodlu dersin kontenjanı", ziplist[1][2],
#      "kişidir.\nKredisi", ziplist[2][0], "olan", ziplist[2][1] , "kodlu dersin kontenjanı", ziplist[2][2],
#      "kişidir.\nKredisi", ziplist[3][0], "olan", ziplist[3][1] , "kodlu dersin kontenjanı", ziplist[3][2], "kişidir.")

###############################################
# GÖREV 8: Aşağıda 2 adet set verilmiştir.
# Sizden istenilen eğer 1. küme 2. kümeyi kapsiyor ise ortak elemanlarını eğer kapsamıyor ise 2. kümenin 1. kümeden farkını yazdıracak fonksiyonu tanımlamanız beklenmektedir.
###############################################

kume1 = set(["data", "python"])
kume2 = set(["data", "function", "qcut", "lambda", "python", "miuul"])

if kume2.issubset(kume1):
    print(kume1.intersection(kume2))
else:
    print(kume2.difference(kume1))



##################################################
# List Comprehensions
##################################################

# ###############################################
# # GÖREV 1: List Comprehension yapısı kullanarak car_crashes verisindeki numeric değişkenlerin isimlerini büyük harfe çeviriniz ve başına NUM ekleyiniz.
# ###############################################
#
# # Beklenen Çıktı
#
# # ['NUM_TOTAL',
# #  'NUM_SPEEDING',
# #  'NUM_ALCOHOL',
# #  'NUM_NOT_DISTRACTED',
# #  'NUM_NO_PREVIOUS',
# #  'NUM_INS_PREMIUM',
# #  'NUM_INS_LOSSES',
# #  'ABBREV']
#
# # Notlar:
# # Numerik olmayanların da isimleri büyümeli.
# # Tek bir list comp yapısı ile yapılmalı.


import seaborn as sns
import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)

df = sns.load_dataset("car_crashes")
df.columns
df.info()

numbercolumns = ["NUM_" + col.upper() if df[col].dtype != "O" else col.upper() for col in df.columns]
print(numbercolumns)


# ###############################################
# # GÖREV 2: List Comprehension yapısı kullanarak car_crashes verisindeki isminde "no" barındırmayan değişkenlerin isimlerininin sonuna "FLAG" yazınız.
# ###############################################
#
import seaborn as sns
import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)

df = sns.load_dataset("car_crashes")
df.columns
df.info()

newcolumns = [col.upper() + "_FLAG" if "no" not in col else col.upper() for col in df.columns]
print(newcolumns)


# # Notlar:
# # Tüm değişken isimleri büyük olmalı.
# # Tek bir list comp ile yapılmalı.
#
# # Beklenen çıktı:
#
# # ['TOTAL_FLAG',
# #  'SPEEDING_FLAG',
# #  'ALCOHOL_FLAG',
# #  'NOT_DISTRACTED',
# #  'NO_PREVIOUS',
# #  'INS_PREMIUM_FLAG',
# #  'INS_LOSSES_FLAG',
# #  'ABBREV_FLAG']



# ###############################################
# # Görev 3: List Comprehension yapısı kullanarak aşağıda verilen değişken isimlerinden FARKLI olan değişkenlerin isimlerini seçiniz ve yeni bir dataframe oluşturunuz.
# ###############################################
import seaborn as sns
import pandas as pd
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 500)

df = sns.load_dataset("car_crashes")
df.columns
df.info()

og_list = ["abbrev", "no_previous"]

newcols = [col for col in df.columns if col not in og_list]
new_df = df[newcols]
new_df.head()

# # Notlar:
# # Önce yukarıdaki listeye göre list comprehension kullanarak new_cols adında yeni liste oluşturunuz.
# # Sonra df[new_cols] ile bu değişkenleri seçerek yeni bir df oluşturunuz adını new_df olarak isimlendiriniz.
#
# # Beklenen çıktı:
#
# #    total  speeding  alcohol  not_distracted  ins_premium  ins_losses
# # 0 18.800     7.332    5.640          18.048      784.550     145.080
# # 1 18.100     7.421    4.525          16.290     1053.480     133.930
# # 2 18.600     6.510    5.208          15.624      899.470     110.350
# # 3 22.400     4.032    5.824          21.056      827.340     142.390
# # 4 12.000     4.200    3.360          10.920      878.410     165.630
#







