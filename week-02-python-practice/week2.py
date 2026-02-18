from contextlib import nullcontext
from json.decoder import NaN

##################################################
# Pandas Alıştırmalar
##################################################

import numpy as np
import seaborn as sns
import pandas as pd
from IPython.core.magic_arguments import argument_group
from numpy.matlib import empty
from pandas.conftest import axis

pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

#########################################
# Görev 1: Seaborn kütüphanesi içerisinden Titanic veri setini tanımlayınız.
#########################################
df = sns.load_dataset("titanic")
df.head()
#########################################
# Görev 2: Yukarıda tanımlanan Titanic veri setindeki kadın ve erkek yolcuların sayısını bulunuz.
#########################################

df["sex"].value_counts()

#########################################
# Görev 3: Her bir sutuna ait unique değerlerin sayısını bulunuz.
#########################################

df.nunique()

#########################################
# Görev 4: pclass değişkeninin unique değerleri bulunuz.
#########################################

df["pclass"].nunique()

#########################################
# Görev 5:  pclass ve parch değişkenlerinin unique değerlerinin sayısını bulunuz.
#########################################

df[["pclass", "parch"]].nunique()

#########################################
# Görev 6: embarked değişkeninin tipini kontrol ediniz. Tipini category olarak değiştiriniz. Tekrar tipini kontrol ediniz.
#########################################

df["embarked"].dtype
df["embarked"] = df["embarked"].astype("category")
df["embarked"].dtype

#########################################
# Görev 7: embarked değeri C olanların tüm bilgelerini gösteriniz.
#########################################

df[df["embarked"] == "C"]


#########################################
# Görev 8: embarked değeri S olmayanların tüm bilgelerini gösteriniz.
#########################################

df[df["embarked"] != "S"]

#########################################
# Görev 9: Yaşı 30 dan küçük ve kadın olan yolcuların tüm bilgilerini gösteriniz.
#########################################

df[(df["age"] < 30) & (df["sex"] == "female")]

#########################################
# Görev 10: Fare'i 500'den büyük veya yaşı 70 den büyük yolcuların bilgilerini gösteriniz.
#########################################

df[(df["fare"] > 500) & (df["age"] > 70)]

#########################################
# Görev 11: Her bir değişkendeki boş değerlerin toplamını bulunuz.
#########################################
#df.isnull().value_counts()

df.isnull().sum()

#########################################
# Görev 12: who değişkenini dataframe'den düşürün.
#########################################

df.drop("who", axis= 1, inplace=True)
df.head()
df.info()

#########################################
# Görev 13: deck değişkenindeki boş değerleri deck değişkenin en çok tekrar eden değeri (mode) ile doldurunuz.
#########################################

df["deck"].fillna(value=df["deck"].mode()[0], inplace=True)
df["deck"]

##

df.loc[df["deck"].isnull(),"deck"] = df.loc[df["deck"].isnull(),"deck"].apply(lambda x: df["deck"].mode()[0])


#########################################
# Görev 14: age değikenindeki boş değerleri age değişkenin medyanı ile doldurun.
#########################################

df.loc[df["age"].isnull(),"age"] = df.loc[df["age"].isnull(),"age"].apply(lambda x: df["age"].median())

df["age"].fillna(value=df["age"].median(), inplace=True)
df["age"]

#########################################
# Görev 15: survived değişkeninin Pclass ve Cinsiyet değişkenleri kırılımınında sum, count, mean değerlerini bulunuz.
#########################################

df.groupby(["pclass", "sex"]).agg({"survived": ["sum", "count", "mean"]})
df.pivot_table("survived", "pclass", "sex", aggfunc= ["sum", "count", "mean"])


#########################################
# Görev 16:  30 yaşın altında olanlar 1, 30'a eşit ve üstünde olanlara 0 vericek bir fonksiyon yazınız.
# Yazdığınız fonksiyonu kullanarak titanik veri setinde age_flag adında bir değişken oluşturunuz oluşturunuz. (apply ve lambda yapılarını kullanınız)
#########################################

def age_flag(value):
    if value < 30:
        return 1
    else:
        return 0

df["age_flag"] = df["age"].apply(lambda value: age_flag(value))
df.head()


#########################################
# Görev 17: Seaborn kütüphanesi içerisinden Tips veri setini tanımlayınız.
#########################################

df2 =sns.load_dataset("tips")
df2.head()
df2.shape

#########################################
# Görev 18: Time değişkeninin kategorilerine (Dinner, Lunch) göre total_bill  değerlerinin toplamını, min, max ve ortalamasını bulunuz.
#########################################

df2.groupby(["time"]).agg({"total_bill": ["sum", "min", "max", "mean"]})

df2.pivot_table("total_bill", "time", aggfunc= ["sum", "min", "max", "mean"])

#########################################
# Görev 19: Günlere ve time göre total_bill değerlerinin toplamını, min, max ve ortalamasını bulunuz.
#########################################

df2.groupby(["time", "day"]).agg({"total_bill": ["sum", "min", "max", "mean"]})

df2.pivot_table("total_bill", "time", "day", aggfunc= ["sum", "min", "max", "mean"])

#########################################
# Görev 20:Lunch zamanına ve kadın müşterilere ait total_bill ve tip  değerlerinin day'e göre toplamını, min, max ve ortalamasını bulunuz.
#########################################

df2[(df2["time"] == "Lunch") & (df2["sex"] == "Female")].groupby(["day"]).agg({"total_bill": ["sum", "min", "max", "mean"], "tip": ["sum", "min", "max", "mean"]})
df2[(df2["time"] == "Lunch") & (df2["sex"] == "Female")].pivot_table(["total_bill", "tip"], "day", aggfunc=["sum", "min", "max", "mean"])

#########################################
# Görev 21: size'i 3'ten küçük, total_bill'i 10'dan büyük olan siparişlerin ortalaması nedir?
#########################################

df2[(df2["size"] < 3) & (df2["total_bill"] > 10)][["total_bill", "tip", "size"]].mean()

#########################################
# Görev 22: total_bill_tip_sum adında yeni bir değişken oluşturun. Her bir müşterinin ödediği totalbill ve tip in toplamını versin.
#########################################

df2["total_bill_tip_sum"] = df2["total_bill"] + df2["tip"]
df2.head()

#########################################
# Görev 23: total_bill_tip_sum değişkenine göre büyükten küçüğe sıralayınız ve ilk 30 kişiyi yeni bir dataframe'e atayınız.
#########################################

df2.sort_values(by= "total_bill_tip_sum", ascending = False, inplace = True)
df2.head()
df3 = df2[:30]
df3
df3.shape
