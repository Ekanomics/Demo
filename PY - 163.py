# # 2. Откройте и прочитайте данные с файла lorum.txt, способом, который рассматривается в видео из пункта 1.

# encoding utf-8 для перевода знаков из кирилицы

# file = open('lorum.txt', encoding='utf-8')
# print(file.read())


# # 3 - Различные моды

# file = open('lorum.txt', 'a+')
# print(file.write('Hello my friend'))


# 4 - Запишите любую информацию в файл с разными значениями mode для записи. Какую разницу при записи файла вы заметили?
# file = open('lorum.txt', 'a+')
# print(file.write('Hello my friend'))


# 5
# with open('lorum.txt', 'a+') as l:
#     l.write('Good evening')
#     l.write('\n123456789')


# 6
# import pandas as pd
# data = pd.read_csv('bikes.csv', nrows=10)
# data.head(10)


# 7 - Посчитайте сумму столбца Rachel1 из файла bikes.csv
# import pandas as pd
# data = pd.read_csv('bikes.csv')
# stolb_summa = data['Rachel1'].sum()
# print(f"Сумма столбца Rachel1: {stolb_summa}")


# 8 - Pandas

# - 8.1 - Часть 1: Чтение данных из csv файла

# import pandas as pd
# import matplotlib.pyplot as plt
#
# plt.style.use('ggplot')
# plt.rcParams['figure.figsize'] = (15, 5)
#
# fixed_df = pd.read_csv('C:/Users/User/Desktop/Coding/Projects/27.03.2024 pp/bikesss.csv',
#                        sep=';', encoding='latin1',
#                        parse_dates=['Date'], dayfirst=True,
#                        index_col='Date')
# pd.set_option('display.max_columns', None)   # отображение полной таблицы
# print(fixed_df[:3]),                         # отображение первых 3 строк
#
# var = fixed_df['Berri 1'][:10],              # отображение данных по Берри 1
# print(var)
#
# fixed_df['Berri 1'].plot()                   # С помощью plot добавление графика
# plt.show()
#
# fixed_df.plot(figsize=(15, 10))
# plt.show()


# - 8.2 - Часть 2: Выбор данных и нахождение наиболее частых жалоб

# import pandas as pd
# import matplotlib.pyplot as plt
#
# plt.style.use('ggplot')
# plt.rcParams['figure.figsize'] = (10, 5)
#
# complaints = pd.read_csv('C:/Users/User/Desktop/Coding/Projects/27.03.2024 pp/311-service-requests.csv')
#
# print(complaints[:5])
#
# print(complaints['Complaint Type'][:5])     # выбор столбца
# print(complaints[:5]['Complaint Type'])     # одинаковый исход
#
# print(complaints[['Complaint Type', 'Borough']])           # Выбор нескольких столбцов
# print(complaints[['Complaint Type', 'Borough']][:10])      # первые 10 строк
#
# # Какой самый частыwй тип жалобы?
# print(complaints['Complaint Type'].value_counts())                         # с помощью value_counts
#
# complaint_counts = complaints['Complaint Type'].value_counts()             # первые 10
# print(complaint_counts[:10])
#
# complaint_counts[:10].plot(kind='bar')
# plt.show()



# - 8.3 - Часть 3: объединение и группировка данных

# import pandas as pd
# import matplotlib.pyplot as plt
# plt.style.use('ggplot')
# plt.rcParams['figure.figsize'] = (10, 5)
#
# bikes = pd.read_csv('C:/Users/User/Desktop/Coding/Projects/27.03.2024 pp/bikes - part3.csv', sep=';', encoding='latin1', parse_dates=['Date'], dayfirst=True, index_col='Date')
# bikes['Berri 1'].plot()
# plt.show()
#
# berri_bikes = bikes[['Berri 1']].copy()        # data frame с дорожкой Берри
# print(berri_bikes[:5])
#
# # print(berri_bikes.index)              # Первый столбец Индекс
# # print(berri_bikes.index.day)          # День месяца для каждой строки
# print(berri_bikes.index.weekday)      # День недели, 0 в нем это понедельник
# berri_bikes.loc[:,'weekday'] = berri_bikes.index.weekday
# print(berri_bikes[:5])
#
# weekday_counts = berri_bikes.groupby('weekday').sum()
# # Добавляем велосипедистов, метод .groupby(), который группирует по одному или нескольким столбцам
# # означает "Сгруппировать строки по дню недели и затем сложить все значения с одинаковым днём недели".
# # weekday_counts = berri_bikes.groupby('weekday').aggregate(sum) - можно и так
# print(weekday_counts)
#
# weekday_counts.index = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
# print(weekday_counts)
# # переименуем 0, 1, 2, 3, 4, 5, 6 в дни недели
#
# weekday_counts.plot(kind='bar')      # В монреале чаще катаются по будням
# plt.show()



# - 8.4 - Часть 4: объединение нескольких dataframe

# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np

# pd.options.display.max_rows = 7
# plt.style.use('ggplot')
# plt.rcParams['figure.figsize'] = (15, 3)
# plt.rcParams['font.family'] = 'sans-serif'
# #
# # weather_2012_final = pd.read_csv('data/weather_2012.csv', index_col='Date/Time')
# # weather_2012_final['Temp (C)'].plot(figsize=(18, 6))


# url_template = "http://climate.weather.gc.ca/climate_data/bulk_data_e.html?format=csv&stationID=5415&Year={year}&Month={month}&timeframe=1&submit=Download+Data"
# url = url_template.format(month=3, year=2012)
#
# weather_mar2012 = pd.read_csv(url, index_col='Date', parse_dates=True, encoding='latin1')
# print(weather_mar2012.head())
                       # Ссылка не сработала, я скачал файл CSV с сайта с нужными мне данными


# weather_data = pd.read_csv('C:/Users/User/Desktop/Coding/Projects/27.03.2024 pp/en_climate_hourly_QC_7035290_03-2012_P1H.csv', encoding='latin1')
# pd.set_option('display.max_columns', None)
# print(weather_data.head())
# Загрузка файла чтобы увидеть заголовки


# weather_mar2012 = pd.read_csv('C:/Users/User/Desktop/Coding/Projects/27.03.2024 pp/en_climate_hourly_QC_7035290_03-2012_P1H.csv', index_col='Date/Time (LST)', parse_dates=True, encoding='latin1')
# print(weather_mar2012)
#
# weather_mar2012["Temp (Â°C)"].plot(figsize=(15, 5))
# plt.show()
# # график температуры
#
# weather_mar2012 = weather_mar2012.dropna(axis=1, how='any')
# print(weather_mar2012[:5])
# # функция dropna удаляет данные, axis=1 удаляет столбцы, how=any означает если хотя бы одно значение пусто удалить
#
# weather_mar2012 = weather_mar2012.drop(['Year', 'Month', 'Day', 'Time (LST)', 'Latitude (y)', 'Climate ID'], axis=1)
# print(weather_mar2012[:5])
#
# # Дневной график температуры
# temperatures = weather_mar2012[[u'Temp (Â°C)']].copy()
# temperatures.loc[:,'Hour'] = weather_mar2012.index.hour
# temperatures.groupby('Hour').aggregate(np.median).plot()
# plt.show()




# - 8.5 - Часть 4: объединение нескольких dataframe

# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np
#
# pd.options.display.max_rows = 7
# plt.style.use('ggplot')
# plt.rcParams['figure.figsize'] = (15, 3)
# plt.rcParams['font.family'] = 'sans-serif'
#
# weather_2012 = pd.read_csv('C:/Users/User/Desktop/Coding/Projects/27.03.2024 pp/en_climate_hourly_QC_7035290_03-2012_P1H.csv', parse_dates=True, index_col='Date/Time (LST)')
# print(weather_2012[:5])
#
# # Операции над строками в pandas
#
# weather_description = weather_2012['Weather']
# is_snowing = weather_description.str.contains('Snow')
# print(is_snowing[:5])
#
# is_snowing_numeric = is_snowing.astype(int)
# is_snowing_numeric.plot(figsize=(15, 5))
# plt.show()
#
# weather_2012.columns = weather_2012.columns.str.replace('Â', '')

# находим снежные дни
# weather_2012['Temp (°C)'].resample('D').median().plot(kind='bar')
#
# is_snowing_numeric = is_snowing.astype(int)
# print(is_snowing_numeric[:10])
# daily_snowing = is_snowing_numeric.resample('ME').mean()
# print(daily_snowing)
# daily_snowing.plot(kind='bar')
# plt.show()
#
#
# #Строим графики температур и снежности вместе
# temperature = weather_2012['Temp (°C)'].resample('D').median()
# is_snowing = weather_2012['Weather'].str.contains('Snow')
# snowiness = is_snowing.astype(int).resample('D').mean()
#
# # Назовем столбцы
# temperature.name = "Temperature"
# snowiness.name = "Snowiness"
#
# stats = pd.concat([temperature, snowiness], axis=1)
# print(stats)
#
# stats.plot(kind='bar')
# plt.show()
#
#
# # Разделим 2 графика
# stats.plot(kind='bar', subplots=True, figsize=(15, 10))
# plt.show()
