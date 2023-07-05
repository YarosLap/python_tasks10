import pandas as pd
import seaborn as sns

# Задача 2. Постройте диаграмму с данными о численности студентов 
# дневной формы обучения южного федерального округа за 2017 год

df = pd.read_csv('/Users/elvis/Desktop/Рабочий стол — MacBook Pro — Ярослав/gb/Python/dz10/data.csv', sep=';',encoding='cp1251')
slice2 = df.loc[33:40, ['Субъект РФ', 'Численность студентов, очная форма, человек, 2017']]
plot = sns.barplot(data=slice2, x='Субъект РФ', y='Численность студентов, очная форма, человек, 2017')
plot.set_xticklabels(plot.get_xticklabels(),rotation = 90)