import pandas as pd
import matplotlib.pyplot as plt




# Задание №2 Чтение и измерение датасета
print("\n\n\n# Задание №2 Чтение и измерение датасета")

df = pd.read_csv('2019.csv')
rows, _ = df.shape
first_5_rows = df.head(5)
print(f'Размер датасета: {rows} записей')
print(f'Первые 5 записей:\n{first_5_rows}')




# Задание №3 Переименование столбцов
print("\n\n\n# Задание №3 Переименование столбцов")

df.rename(columns={
    'Overall rank': 'Место в рейтинге',
    'Country or region': 'Страна или регион',
    'Score': 'Баллы',
    'GDP per capita': 'ВВП на душу населения',
    'Social support': 'Социальная поддержка',
    'Healthy life expectancy': 'Ожидаемая продолжительность здоровой жизни',
    'Freedom to make life choices': 'Свобода жизненных выборов',
    'Generosity': 'Щедрость',
    'Perceptions of corruption': 'Восприятие коррупции'
}, inplace=True)
print(df)




# Задание №4 Определение характеристик датасета
print("\n\n\n# Задание №4 Определение характеристик датасета")

print("Характеристики датасета:")
print(df.describe())
print(df.info())




# Задание №5 Работа со срезами
print("\n\n\n# Задание №5 Работа со срезами")

cut1 = df[['Место в рейтинге', 'Ожидаемая продолжительность здоровой жизни']]
print(f'Столбцы "Место в рейтинге" и "Ожидаемая продолжительность здоровой жизни":\n{cut1}')

cut2 = df.loc[:, 'Место в рейтинге':'Социальная поддержка']
print(f'Срез столбцов начиная с "Место в рейтинге" и заканчивая "Социальная поддержка":\n{cut2}')

cut3 = df.iloc[67:72, 0:4]
print(f'Срез строк 67:72 - столбцов 0:4 :\n{cut3}')

l1 = df['Баллы'].tolist()
print(f'Список значений столбца "Баллы":\n{l1}')

l_names = df.columns.tolist()
print(f'Названия столбцов:\n{l_names}')

cut21 = df[['Страна или регион', 'ВВП на душу населения']]
print(f'Столбцы "Страна или регион", "ВВП на душу населения":\n{cut21}')

l2 = df['Страна или регион'].tolist()
print(f'Список значений столбца "Страна или регион":\n{l2}')

cut23 = df.iloc[60:70, 1:3]
print(f'Строки 60:70 - столбцы 1:3:\n{cut23}')

place_russia = df[df['Страна или регион'] == 'Russia'].iloc[0]['Место в рейтинге']
print(f'Место России в рейтинге: {place_russia}')




# Задание №6 Добавление новых строк и столбцов
print('\n\n\n# Задание №6 Добавление новых строк и столбцов')

new_c = df['Сумма щедрости и восприятия коррупции'] = df['Щедрость'] + df['Восприятие коррупции']
print(new_c)

new_row = {'Место в рейтинге': 100, 'Страна или регион': 'Country', 'Баллы': 100}
df = pd.concat([df, pd.DataFrame([new_row])], ignore_index=True)
print(df.iloc[-1])

df = pd.concat([df, pd.DataFrame([df.sum(axis=0)])], ignore_index=True)
print(df.iloc[-1])




# Задание №7 Удаление строк и столбцов методом drop()
print('\n\n\n# Задание №7 Удаление строк и столбцов методом drop()')

df = df.drop(['Сумма щедрости и восприятия коррупции'], axis=1)
print(df.columns.tolist())

df = df.drop([df.index[-1], df.index[-2]], axis=0)
print(df.iloc[-1])




# Задание №8 Уникальные значения
print('\n\n\n# Задание №8 Уникальные значения')

# print(df['Страна или регион'].unique())
# print(len(df['Страна или регион'].unique()))
# print(df['Страна или регион'].value_counts())

print(df['Баллы'].unique())
print(len(df['Баллы'].unique()))
print(df['Баллы'].value_counts())




# Задание №9 Группировка данных методом groupby()
print('\n\n\n# Задание №9 Группировка данных методом groupby()')

df['Баллы_new'] = round(df['Баллы'])
print(df['Баллы_new'])

print(df.groupby('Баллы_new').count())
print(df.groupby('Баллы_new')['Баллы'].agg(['sum', 'mean', 'median']))




# Задание №10 Сводные таблицы. Метод pivot_table()
print('\n\n\n# Задание №10 Сводные таблицы. Метод pivot_table()')

df['ВВП_new'] = round(df['ВВП на душу населения'], ndigits=1)
df['Свободы_new'] = round(df['Свобода жизненных выборов'], ndigits=1)

# print("Таблица социальной поддержки населения по общему рейтингу страны и ВВП на душу населения")
# print(pd.pivot_table(df, index=['Баллы_new'], columns=['ВВП_new'], values='Социальная поддержка', aggfunc='mean'))

print("Таблица продолжительности жизни населения по уровню свобод и ВВП на душу населения")
print(
    pd.pivot_table(
        df,
        index=['Свободы_new'],
        columns=['ВВП_new'],
        values='Ожидаемая продолжительность здоровой жизни',
        aggfunc='mean'
    )
)

df = df.drop(['ВВП_new'], axis=1)
df = df.drop(['Свободы_new'], axis=1)




# Задание №11 Сортировка данных. Метод sort_values()
print('\n\n\n# Задание №11 Сортировка данных. Метод sort_values()')

min_vvp = df.sort_values(by='ВВП на душу населения').iloc[0]['ВВП на душу населения']
max_vvp = df.sort_values(by='ВВП на душу населения', ascending=False).iloc[0]['ВВП на душу населения']
print(f'Максимальное ВВП: {max_vvp}\nМинимальное ВВП: {min_vvp}')




# Задание №12 Фильтрация данных по условию
print('\n\n\n# Задание №12 Фильтрация данных по условию')

print(df[df['Страна или регион'] == 'Norway'])
print(df[df['Ожидаемая продолжительность здоровой жизни'] > 1])
print(df[df['Страна или регион'].str.startswith('F')])
print(df[(df['ВВП на душу населения'] > 1) & (df['Социальная поддержка'] > 1.5)])




# Задание №13 Построение графиков
print('\n\n\n# Задание №13 Построение графиков')

# df.plot(x='Место в рейтинге', y='ВВП на душу населения')
# df.plot.hist(y='ВВП на душу населения')
# df.plot.scatter(x='Место в рейтинге', y='ВВП на душу населения')

df.plot(x='Место в рейтинге', y='Свобода жизненных выборов', kind='line')
df.plot.hist(y='Ожидаемая продолжительность здоровой жизни')
for c in df.columns:
    if df[c].dtype == float and c not in ('Баллы', 'Баллы_new'):
        df.plot.scatter(x='Место в рейтинге', y=c)
plt.show()




# Задание №14 Расчет коэффициента корреляции
print('\n\n\n# Задание №14 Расчет коэффициента корреляции')

m = ['Место в рейтинге']
for c in df.columns:
    if df[c].dtype == float and c not in ('Баллы', 'Баллы_new'):
        m.append(c)
correlation_matrix = df[m].corr()

ranking_correlations = correlation_matrix['Место в рейтинге']
ranking_correlations = ranking_correlations.drop('Место в рейтинге')
print(f"Поле с максимальной степенью влияния на место в рейтинге: {ranking_correlations.abs().idxmax()}\
{ranking_correlations[ranking_correlations.abs().idxmax()]}")
