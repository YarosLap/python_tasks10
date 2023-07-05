import pandas as pd
import seaborn as sns

# Задача 1. Найдите, какая область центрального федерального округа имела наибольшую численность 
# студентов вечерней формы обучения в 2015 году.

df = pd.read_csv('/Users/elvis/Desktop/Рабочий стол — MacBook Pro — Ярослав/gb/Python/dz10/data.csv', sep=';',encoding='cp1251')
slice1 = df.loc[2:19, ['Субъект РФ', 'Численность студентов очно-заочная (вечерняя) форма, человек, 2015']]
print(slice1.max())