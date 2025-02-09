import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import scipy.stats as st
directory = os.getcwd()
print("The Current working directory is :", directory)
file = 'Myers Briggs Table_S1.csv'
data = pd.read_csv(file)

# zamiana zmiennych na kategorialne
data['ACTIVITY LEVEL'] = data['ACTIVITY LEVEL'].astype('category')
data['ACTIVITY LEVEL']=data['ACTIVITY LEVEL'].cat.reorder_categories(['Low',
                                                        'Moderate',
                                                        'High'], ordered=True)
data['SEX'] = data['SEX'].astype('category')
data['POSTURE']= data['POSTURE'].astype('category')
data['MBTI']= data['MBTI'].astype('category')

data['WEIGHT_KG']= data['WEIGHT']*0.454 #przekonwertowałam funty na kg tworząc nową zmienną


data['HEIGHT_CM']= data['HEIGHT']*2.54 #przekonwertowałam cale na cm tworząc nową zmienną


#SEX
# print(data['SEX'].mode())
# print(data['SEX'].value_counts())

# wykres kołowy
# x=data['SEX']
# plt.pie(data['SEX'].value_counts(), labels=['Female', 'Male'], autopct='%0f%%')
# plt.show

# # # # wykres kolumnowy
# czestosci1= data['SEX'].value_counts()
# data= czestosci1.reset_index()
# print(data)
# data.columns= ['SEX', 'licznik']
# plt.bar(data['SEX'], data.licznik, color='#a83253')
# plt.yticks(range(0,50, 5))
# plt.ylabel('Liczba badanych')
# plt.xlabel('Płeć')
# plt.show()

# # ACTIVITY LEVEL
# print(data['ACTIVITY LEVEL'].mode()) #dominanta najwięcej jest aktywności niskiej
# print(data['ACTIVITY LEVEL'].value_counts()) #aktywność niska=74, umiarkowana=17, wysoka=6

# # wykres kolumnowy
# czestosci1= data['ACTIVITY LEVEL'].value_counts()
# data= czestosci1.reset_index()
# print(data)
# data.columns= ['ACTIVITY LEVEL', 'licznik']
# plt.bar(data['ACTIVITY LEVEL'], data.licznik, color='#a83253')
# plt.yticks(range(0,100, 5))
# plt.ylabel('Liczba badanych')
# plt.xlabel('Poziom aktywności fizycznej')
# plt.show()


# # TYPY BÓLU
# # PAIN 1
# print(data['PAIN 1'].mode()) #najczęściej pojawia się 0- brak bólu
# print(data['PAIN 1'].mean()) #średnia 2,14
# print(data['PAIN 1'].max()) #9.5
# print(data['PAIN 1'].min()) #0
# print(data['PAIN 1'].median()) #1
# print(data['PAIN 1'].var()) #6,62
# print(data['PAIN 1'].std()) #2,57
# print(data['PAIN 1'].quantile(0.25)) #0
# print(data['PAIN 1'].quantile(0.75)) #4
# print(data['PAIN 1'].value_counts()) #44 osoby nie odczuwają tego bólu

# plt.hist(data['PAIN 1'], bins= range(0, 11, 1), color='#a83253',edgecolor='black')
# plt.xticks(range(0,11,1))
# plt.ylabel('Liczba badanych')
# plt.xlabel('Skala bólu typu 1')
# plt.show()

# PAIN 2
# print(data['PAIN 2'].mode()) #najczęściej pojawia się 0- brak bólu
# print(data['PAIN 2'].mean()) #średnia 3,75
# print(data['PAIN 2'].max()) #10
# print(data['PAIN 2'].min()) #0
# print(data['PAIN 2'].median()) #3
# print(data['PAIN 2'].var()) #10,18
# print(data['PAIN 2'].std()) #3,19
# print(data['PAIN 2'].quantile(0.25)) #0
# print(data['PAIN 2'].quantile(0.75)) #7
# print(data['PAIN 2'].value_counts()) #26 osób nie odczuwa tego bólu

# plt.hist(data['PAIN 2'], bins= range(0, 11, 1), color='#a83253',edgecolor='black')
# plt.xticks(range(0,11,1))
# plt.ylabel('Liczba badanych')
# plt.xlabel('Skala bólu typu 2')
# plt.show()

# PAIN 3
# print(data['PAIN 3'].mode()) #najczęściej pojawia się 0- brak bólu
# print(data['PAIN 3'].mean()) #średnia 1,94
# print(data['PAIN 3'].max()) #10
# print(data['PAIN 3'].min()) #0
# print(data['PAIN 3'].median()) #0.5
# print(data['PAIN 3'].var()) #6,70
# print(data['PAIN 3'].std()) #2,59
# print(data['PAIN 3'].quantile(0.25)) #0
# print(data['PAIN 3'].quantile(0.75)) #3,5
# print(data['PAIN 3'].value_counts()) #48 osób nie odczuwa tego bólu

# plt.hist(data['PAIN 3'], bins= range(0, 11, 1), color='#a83253',edgecolor='black')
# plt.xticks(range(0,11,1))
# plt.ylabel('Liczba badanych')
# plt.xlabel('Skala bólu typu 3')
# plt.show()

# PAIN 4
# print(data['PAIN 4'].mode()) #najczęściej pojawia się 0- brak bólu
# print(data['PAIN 4'].mean()) #średnia 2,53
# print(data['PAIN 4'].max()) #10
# print(data['PAIN 4'].min()) #0
# print(data['PAIN 4'].median()) #0
# print(data['PAIN 4'].var()) #9,68
# print(data['PAIN 4'].std()) #3,11
# print(data['PAIN 4'].quantile(0.25)) #0
# print(data['PAIN 4'].quantile(0.75)) #5
# print(data['PAIN 4'].value_counts()) #49 osób nie odczuwa tego bólu

# plt.hist(data['PAIN 4'], bins= range(0, 11, 1), color='#a83253',edgecolor='black')
# plt.xticks(range(0,11,1))
# plt.ylabel('Liczba badanych')
# plt.xlabel('Skala bólu typu 4')
# plt.show()

# Porównanie wszystkich typów bólu na jednym histogramie
# plt.style.use('seaborn-deep')
# x = data['PAIN 1']
# y = data['PAIN 2']
# x1 = data['PAIN 3']
# y1 = data['PAIN 4']
# bins = np.linspace(0, 11, 10)
# plt.xticks(range(0,11,1))
# plt.hist([x, y, x1, y1], bins, label=['PAIN 1', 'PAIN 2', 'PAIN 3', 'PAIN 4'])
# plt.legend(loc='upper right')
# plt.ylabel('Liczba badanych')
# plt.xlabel('Poziom na skali bólu')
# plt.show()


#POSTURE
# print(data['POSTURE'].mode()) #najczęstszy typ postawy to B
# print(data['POSTURE'].value_counts()) #A-22, B-36, C-19, D-20

# czestosci2= data['POSTURE'].value_counts()
# data= czestosci2.reset_index()
# print(data)
# data.columns= ['POSTURE', 'licznik']
# plt.bar(data['POSTURE'], data.licznik, color='#a83253')
# plt.yticks(range(0,50, 5))
# plt.xlabel('Typ postawy ciała')
# plt.ylabel('Liczba badanych')
# plt.show()


# WEIGHT_KG
# print(data['WEIGHT_KG'].mode()) #68.10, 72.64, 90.80 dominanta
# print(data['WEIGHT_KG'].mean()) #72,38 średnia
# print(data['WEIGHT_KG'].median()) #71,28 mediana
# print(data['WEIGHT_KG'].var()) #270,04 wariancja
# print(data['WEIGHT_KG'].std()) #16,43 odchylenie standardowe
# print(data['WEIGHT_KG'].quantile(0.25)) #61,29 dolny kwartyl
# print(data['WEIGHT_KG'].quantile(0.75)) #83,08 górny kwartyl
# print(data['WEIGHT_KG'].max()) #119,40 maksimum
# print(data['WEIGHT_KG'].min()) #30,87 minimum

# plt.boxplot(data['WEIGHT_KG'])     #wykres pudełkowy
# plt.title('WAGA')
# plt.yticks(range(0,130, 10))
# plt.show()

# MBTI
# print(data['MBTI'].mode()) #najczęstszy typ to ESFP
# print(data['MBTI'].value_counts()) #ESFP=12, ESFJ=11, ENFP=10, ESTP=10, ESTJ=7, ISFP=7, ISTJ=6, ENFJ=5, ENTJ=5, ENTP=5, INFP=5, ISFJ=5, INFJ=4, ISTP=4, INTJ=1
# data.MBTI.value_counts().plot.bar()
# plt.show()


# E I
# print(data['E'].mode()) #16 i 18
# print(data['E'].mean()) #12,69
# print(data['E'].median()) #13
# print(data['E'].var()) #32,69
# print(data['E'].std()) #5,72
# print(data['E'].quantile(0.25)) #8
# print(data['E'].quantile(0.75)) #18
# print(data['E'].max()) #21
# print(data['E'].min()) #2
# print(data['E'].value_counts()) #najwięcej jest 18 i 16

# plt.hist(data['E'], bins= range(0, 25), edgecolor='black')
# plt.yticks(range(0,10, 1))
# plt.ylabel('Liczba badanych')
# plt.xlabel('Wartość Ekstrawertyzmu')
# plt.show()

# print(data['I'].mode()) #3 i 5
# print(data['I'].mean()) #8,29
# print(data['I'].median()) #8
# print(data['I'].var()) #32,46
# print(data['I'].std()) #5,70
# print(data['I'].quantile(0.25)) #3
# print(data['I'].quantile(0.75)) #13
# print(data['I'].max()) #19
# print(data['I'].min()) #0
# print(data['I'].value_counts()) #najwięcej wartości 3 i 5

# plt.hist(data['I'], bins= range(0, 25), edgecolor='black')
# plt.yticks(range(0,10, 1))
# plt.ylabel('Liczba badanych')
# plt.xlabel('Wartość Introwertyzmu')
# plt.show()

# podwójny histogram E i I
# x = data['E']
# y= data['I']
# bins= range(0, 22)
# plt.hist(x, bins, alpha=0.3, label='E', edgecolor='k')
# plt.hist(y, bins, alpha=0.3, label='I', edgecolor='k')
# plt.legend()
# plt.show()

# plt.style.use('seaborn-deep')
# x = data['E']
# y = data['I']
# bins = np.linspace(0, 25, 30)
# plt.hist([x, y], bins, label=['E', 'I'])
# plt.legend(loc='upper right')
# plt.xlabel('Wartość cechy')
# plt.ylabel('Liczba badanych')
# plt.show()

# S i N

# print(data['S'].mode()) #14 i 17
# print(data['S'].mean()) #15,13
# print(data['S'].median()) #15
# print(data['S'].var()) #23,37
# print(data['S'].std()) #4,83
# print(data['S'].quantile(0.25)) #12
# print(data['S'].quantile(0.75)) #19
# print(data['S'].max()) #25
# print(data['S'].min()) #5
# print(data['S'].value_counts()) #najwięcej wartości 14 i 17

# plt.hist(data['S'], bins= range(0, 25), edgecolor='black')
# plt.yticks(range(0,10, 1))
# plt.ylabel('Liczba badanych')
# plt.xlabel('Wartość Poznania')
# plt.show()

# print(data['N'].mode()) #9 i 12
# print(data['N'].mean()) #11,04
# print(data['N'].median()) #11
# print(data['N'].var()) #22,40
# print(data['N'].std()) #4,73
# print(data['N'].quantile(0.25)) #7
# print(data['N'].quantile(0.75)) #14
# print(data['N'].max()) #21
# print(data['N'].min()) #1
# print(data['N'].value_counts()) #najwięcej wartości 9 i 12
#
# plt.hist(data['N'], bins= range(0, 25), edgecolor='black')
# plt.yticks(range(0,10, 1))
# plt.ylabel('Liczba badanych')
# plt.xlabel('Wartość Intuicji')
# plt.show()

# # podwójny histogram
# x = data['S']
# y= data['N']
# bins= range(0, 22)
# plt.hist(x, bins, alpha=0.3, label='S', edgecolor='k')
# plt.hist(y, bins, alpha=0.3, label='N', edgecolor='k')
# plt.legend()
# plt.show()

# plt.style.use('seaborn-deep')
# x = data['S']
# y = data['N']
# bins = np.linspace(0, 25, 30)
# plt.hist([x, y], bins, label=['S', 'N'])
# plt.legend(loc='upper right')
# plt.xlabel('Wartość cechy')
# plt.ylabel('Liczba badanych')
# plt.show()


# T i F
# print(data['T'].mode()) #12
# print(data['T'].mean()) #10.5
# print(data['T'].median()) #11
# print(data['T'].var()) #28,44
# print(data['T'].std()) #5,33
# print(data['T'].quantile(0.25)) #6
# print(data['T'].quantile(0.75)) #14
# print(data['T'].max()) #22
# print(data['T'].min()) #0
# print(data['T'].value_counts()) #najwięcej wartości 12
#
# plt.hist(data['T'], bins= range(0, 25), edgecolor='black')
# plt.yticks(range(0,10, 1))
# plt.ylabel('Liczba badanych')
# plt.xlabel('Wartość Myślenia')
# plt.show()

# print(data['F'].mode()) #12
# print(data['F'].mean()) #13,44
# print(data['F'].median()) #13
# print(data['F'].var()) #28,06
# print(data['F'].std()) #5,30
# print(data['F'].quantile(0.25)) #10
# print(data['F'].quantile(0.75)) #18
# print(data['F'].max()) #24
# print(data['F'].min()) #2
# print(data['F'].value_counts()) #najwięcej wartości 12
#
# plt.hist(data['F'], bins= range(0,25), edgecolor='black')
# plt.yticks(range(0,10, 1))
# plt.ylabel('Liczba badanych')
# plt.xlabel('Wartość Odczuwania')
# plt.show()

# x = data['T']
# y= data['F']
# bins= range(0, 22)
# plt.hist(x, bins, alpha=0.3, label='T', edgecolor='k')
# plt.hist(y, bins, alpha=0.3, label='F', edgecolor='k')
# plt.legend()
# plt.show()

# plt.style.use('seaborn-deep')
# x = data['T']
# y = data['F']
# bins = np.linspace(0, 25, 30)
#
# plt.hist([x, y], bins, label=['T', 'F'])
# plt.legend(loc='upper right')
# plt.ylabel('Liczba badanych')
# plt.xlabel('Wartość cechy')
# plt.show()

# J i P
# print(data['J'].mode()) #2 i 17
# print(data['J'].mean()) #10,32
# print(data['J'].median()) #11
# print(data['J'].var()) #32,80
# print(data['J'].std()) #5,73
# print(data['J'].quantile(0.25)) #5
# print(data['J'].quantile(0.75)) #16
# print(data['J'].max()) #20
# print(data['J'].min()) #0
# print(data['J'].value_counts()) #najwięcej wartości 17 i 2

# plt.hist(data['J'], bins= range(0, 25), edgecolor='black')
# plt.yticks(range(0,10, 1))
# plt.ylabel('Liczba badanych')
# plt.xlabel('Wartość Osądzania')
# plt.show()

# print(data['P'].mode()) #5 i 20
# print(data['P'].mean()) #11,68
# print(data['P'].median()) #11
# print(data['P'].var()) #32,61
# print(data['P'].std()) #5,71
# print(data['P'].quantile(0.25)) #6
# print(data['P'].quantile(0.75)) #17
# print(data['P'].max()) #22
# print(data['P'].min()) #2
# print(data['P'].value_counts()) #najwięcej wartości 20 i 5

# plt.hist(data['P'], bins= range(0, 25), edgecolor='black')
# plt.yticks(range(0,10, 1))
# plt.ylabel('Liczba badanych')
# plt.xlabel('Wartość Obserwacji')
# plt.show()

# plt.style.use('seaborn-deep')
# x = data['J']
# y = data['P']
# bins = np.linspace(0, 25, 30)
# plt.hist([x, y], bins, label=['J', 'P'])
# plt.legend(loc='upper right')
# plt.xlabel('Wartość cechy')
# plt.ylabel('Liczba badanych')
# plt.show()

# //ZALEŻNOŚĆ MIĘDZY TYPEM OSOBOWOŚCI A POSTURĄ//
# pogrupowanie typów osobowości wedle ich dominant typu postury
# print(data.groupby('MBTI')['POSTURE'].agg(pd.Series.mode))
# # typy ekstrawertyczne mają głównie posturę typu B, z kolei typy Introwertyczne D(ewentualnie C)


# data_crosstab1=(pd.crosstab(data['MBTI'], data['POSTURE']))
# print(data_crosstab1)
# print(st.chi2_contingency(data_crosstab1))
# # X2 = 75,8058, p=0,0010, df=42
# # Xalfa=66.2062 < Xobliczone = 75,8058 --> odrzucenie H0, czyli obliczam korelację
# X2 = st.chi2_contingency(data_crosstab1)[0]
# n = np.sum(np.array(data_crosstab1))
# minDim = min(data_crosstab1.shape)-1
# V = np.sqrt((X2/n) / minDim)
# print(V)
# # VCRamer=0,510

# sns.catplot(data, x="POSTURE", y="MBTI")
# plt.show()
# ekstrawertycy=data[data['E'] > data['I']]
# introwertycy= data[data['I']>= data['E']]
# fig, ax =plt.subplots(1,2)
# sns.countplot( x = introwertycy['POSTURE'], ax=ax[0],  order = introwertycy['POSTURE'].value_counts().index)
# sns.countplot( x = ekstrawertycy['POSTURE'], ax=ax[1], order = introwertycy['POSTURE'].value_counts().index)
# ax[1].set_title("E -extrawertycy")
# ax[0].set_title("I -introwertycy")
# plt.show()


# poznanie=data[data['S'] > data['N']]
# intuicja= data[data['N']>= data['S']]
# fig, ax =plt.subplots(1,2)
# sns.countplot( x = intuicja['POSTURE'], ax=ax[0],  order = intuicja['POSTURE'].value_counts().index)
# sns.countplot( x = poznanie['POSTURE'], ax=ax[1], order = intuicja['POSTURE'].value_counts().index)
# ax[1].set_title("S -poznanie")
# ax[0].set_title("N -intuicja")
# plt.show()


# myślenie=data[data['T'] > data['F']]
# odczuwanie= data[data['F']>= data['T']]
# fig, ax =plt.subplots(1,2)
# sns.countplot( x = odczuwanie['POSTURE'], ax=ax[0],  order = odczuwanie['POSTURE'].value_counts().index)
# sns.countplot( x = myślenie['POSTURE'], ax=ax[1], order = odczuwanie['POSTURE'].value_counts().index)
# ax[1].set_title("T -myślenie")
# ax[0].set_title("F -odczuwanie")
# plt.show()


# osądzanie=data[data['J'] > data['P']]
# obserwacja= data[data['P']>= data['J']]
# fig, ax =plt.subplots(1,2)
# sns.countplot( x = obserwacja['POSTURE'], ax=ax[0],  order = obserwacja['POSTURE'].value_counts().index)
# sns.countplot( x = osądzanie['POSTURE'], ax=ax[1], order = obserwacja['POSTURE'].value_counts().index)
# ax[1].set_title("J -osądzanie")
# ax[0].set_title("P -obserwacja")
# plt.show()


# //ZALEŻNOŚĆ MIĘDZY WAGĄ A BÓLEM TYPU 1
# print(st.pearsonr(data['WEIGHT_KG'],data['PAIN 1']))
# współczynnik p > 0.05 dlatego nie ma związku

# //ZALEŻNOŚĆ MIĘDZY WAGĄ A BÓLEM TYPU 2
# print(st.pearsonr(data['WEIGHT_KG'],data['PAIN 2']))
# współczynnik p > 0.05 dlatego nie ma związku

# //ZALEŻNOŚĆ MIĘDZY WAGĄ A BÓLEM TYPU 3
# print(st.pearsonr(data['WEIGHT_KG'],data['PAIN 3']))
# współczynnik p > 0.05 dlatego nie ma związku

# //ZALEŻNOŚĆ MIĘDZY WAGĄ A BÓLEM TYPU 4
# print(st.pearsonr(data['WEIGHT_KG'],data['PAIN 4']))
# współczynnik p < 0,05 dlatego istnieje związek o bardzo słabej sile lub jego brak (r=0,22), po próbie stworzenia wykresu dla tych zmiennych widzimy, że tego związku nie ma
#
# plt.scatter(data['WEIGHT_KG'], data['PAIN 4'])
# plt.xlabel('waga')
# plt.ylabel('skala bólu 4')
# plt.show()

# //ZWIĄZEK MIĘDZY POZIOMEM AKTYWNOŚCI A POSTURĄ
# data_crosstab1=(pd.crosstab(data['ACTIVITY LEVEL'], data['POSTURE']))
# print(data_crosstab1)
# print(st.chi2_contingency(data_crosstab1))
# brak związku

# //ZALEŻNOŚĆ MIĘDZY POZIOMEM INTROWERTYZMU A BÓLEM TYPU 1 
# print(st.pearsonr(data['I'],data['PAIN 1']))
# korelacja = 0,1884, p = 0,0645. p > 0,05, brak związku między zmiennymi

# //ZALEŻNOŚĆ MIĘDZY POZIOMEM EKSTRAWERTYZMU A BÓLEM TYPU 1 
# print(st.pearsonr(data['E'],data['PAIN 1']))
# korelacja = -0,1232, p = 0,0723. p > 0,05, brak związku między zmiennymi

# //ZALEŻNOSĆ MIĘDZY POZIOMEM AKTYWNOSCI A POZIOMEM OCENIAJĄCY
# print(st.spearmanr(data['ACTIVITY LEVEL'], data['J']))
#korelacja = -0,1247, p=0,2232. p>0,005, brak związku między zmiennymi

# //ZALEŻNOŚĆ MIĘDZY POZIOMEM OCENIAJĄCY A BÓLEM TYPU 3
# print(st.pearsonr(data['J'],data['PAIN 3']))
# korelacja = 0,1692, p = 0,0975. p > 0,05, brak związku między zmiennymi

# //ZALEŻNOSĆ MIĘDZY PŁCIĄ A POZIOMEM OCENIAJĄCY
# data_crosstab1=(pd.crosstab(data['SEX'], data['J']))
# print(data_crosstab1)
# print(st.chi2_contingency(data_crosstab1))
# # # X2=37,38, p=0,01, df=20
# # # Xalfa=28,41 < Xobliczone=37,38 --> odrzucenie H0, czyli obliczam korelację
# X2 = st.chi2_contingency(data_crosstab1)[0]
# n = np.sum(np.array(data_crosstab1))
# minDim = min(data_crosstab1.shape)-1
# V = np.sqrt((X2/n) / minDim)
# print(V)
# # # V=0,62, czyli umiarkowana siła związku

# x=data.groupby('SEX')['J'].mean()
# data=x.reset_index()
# print(data)
# plt.bar(data.SEX, data.J, color='#a83253')
# plt.xlabel("Płeć")
# plt.ylabel("Średnia wartość J")
# plt.show

# //ZALEŻNOSĆ MIĘDZY PŁCIĄ A POZIOMEM AKTYWNOSCI
# data_crosstab1=(pd.crosstab(data['ACTIVITY LEVEL'], data['SEX']))
# print(data_crosstab1)
# print(st.chi2_contingency(data_crosstab1))
# # # X2=7,87, p=0,019, df=2
# # # Xalfa=4,60 < Xobliczone=7,87 --> odrzucenie H0, czyli obliczam korelację
# X2 = st.chi2_contingency(data_crosstab1)[0]
# n = np.sum(np.array(data_crosstab1))
# minDim = min(data_crosstab1.shape)-1
# V = np.sqrt((X2/n) / minDim)
# print(V)
# #V=0,28, czyli słaba korelacja

# *MIEJSCE NA WYKRES*
