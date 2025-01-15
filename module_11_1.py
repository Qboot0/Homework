#pandas
import pandas as pd

data = pd.read_csv('data.csv')

print("Имена столбцов:", data.columns)

average_value = data['Column3'].mean()

print("Среднее значение Column3:", average_value)

#matplotlib
import matplotlib
matplotlib.use('Agg')  

import matplotlib.pyplot as plt


x = [1, 2, 3, 4, 5]
y = [2, 3, 5, 7, 11]


plt.plot(x, y, marker='o')
plt.title('Пример линейного графика')
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.grid()
plt.savefig('plot.png') 
