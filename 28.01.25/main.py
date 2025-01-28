import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Шаг 1: Считываем данные из Excel
file_path = 'data.xlsx'  # Путь к файлу Excel
df = pd.read_excel(file_path)

# Проверяем структуру данных
print(df.head())  # Вывод первых строк для проверки

# Шаг 2: Построение графика
plt.figure(figsize=(16, 6))  # Размер окна графика

# Используем данные из DataFrame
plt.plot(df['Lesson'], df['Lesson 1'], marker='o', label='Зависимость y от x')

# Настройка графика
plt.title('График из Excel')
plt.xlabel('Ось X')
plt.ylabel('Ось Y')
plt.legend()
plt.grid(True)  # Включить сетку

# Шаг 3: Отображаем график
plt.show()
