import pandas as pd
import seaborn as sns

# Задача 3. Постройте диаграмму количества студентов заочной формы обучения за 2019 год по всем регионам, 
# в которых общее количество студентов не превышает 10000 за данный год.

df = pd.read_csv('/Users/elvis/Desktop/Рабочий стол — MacBook Pro — Ярослав/gb/Python/dz10/data.csv', sep=';',encoding='cp1251')
slice3 = df[df['Численность студентов заочная форма, человек, 2019'] < 10000]
plot = sns.barplot(data=slice3, x='Субъект РФ', y='Численность студентов заочная форма, человек, 2019')
plot.set_xticklabels(plot.get_xticklabels(),rotation = 90)