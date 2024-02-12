import random
import pandas as pd

lst = ['robot'] * 10
lst += ['human'] * 10
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

# Получение уникальных значений столбца
unique_values = data['whoAmI'].unique()

# Создание новых столбцов на основе уникальных значений
for value in unique_values:
    data[value] = (data['whoAmI'] == value).astype(int)

# Удаление исходного столбца
data.drop('whoAmI', axis=1, inplace=True)

data.head()