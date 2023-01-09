import os
import pandas as pd


directory = os.getcwd()
print("The Current working directory is :", directory)
file = 'Myers Briggs Table_S1.csv'
data = pd.read_csv(file)
# print(data)
#
# # data.info()
# # print(len(data)) #97
# # print(len(data.columns)) #20
# #
# # print(data.shape) #97x20
# #
# # print(data.columns) #nazwy kolumn
# # print(data.index) #etykiety wierszy
#
# print(data.AGE.describe) #informacje o danych numerycznych
# print(data.SEX.value_counts) #informacje o danych nominalnych
#
# print(data.dtypes) # informacje o typach zmiennych


# warunek1 = data.SEX.isin(['Female'])   //wyświetlanie danych pod danym warunkiem- filtracja samych kobiet z grupy badanych
# print(data[warunek1])

# // Uporządkowanie zmiennej ACTIVITY LEVEL- nadanie kategorii, uporządkowanie jako zmienna porządkowa //
data['ACTIVITY LEVEL'] = data['ACTIVITY LEVEL'].astype('category')
# print(data['ACTIVITY LEVEL'].cat.categories)
data['ACTIVITY LEVEL']=data['ACTIVITY LEVEL'].cat.reorder_categories(['Low',
                                                        'Moderate',
                                                        'High'], ordered=True)
# print(data['ACTIVITY LEVEL'].cat.ordered)
#
# print(data['ACTIVITY LEVEL'])
# Zmienna kategorialna płeć
data['SEX'] = data['SEX'].astype('category')
# print(data['SEX'].cat.categories)
# print(data['SEX'])
# Mam problem ze zmienną skali bólu- jest porządkowa czy ilościowa? i czy w ogóle zmieniać ją w zmienną kategorialną

data['POSTURE']= data['POSTURE'].astype('category')
# print(data['POSTURE'])

data['MBTI']= data['MBTI'].astype('category') 

data.WEIGHT= data.WEIGHT*0.454 #przekonwertowałam funty na kg

data.HEIGHT= data.HEIGHT*2.54 #przekonwertowałam cale na cm


data.WEIGHT.count()  #podliczenie wszystkich wartości zmiennej
print(data.WEIGHT.count())

print(data['WEIGHT'].mean()) #wyznaczenie średniej

print(data['WEIGHT'].min()) #wyznaczenie wartości minimalnej
