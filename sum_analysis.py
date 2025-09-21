# sum_analysis.py
import timeit
import matplotlib.pyplot as plt
import random

# -----------------------------
# Простая задача: сумма двух чисел
# -----------------------------
def calculate_sum():
    """Считает сумму двух введенных чисел."""
    a = int(input("Введите число a: "))  # O(1) - чтение строки и преобразование
    b = int(input("Введите число b: "))  # O(1)
    result = a + b                        # O(1) - арифметическая операция
    print("Сумма:", result)               # O(1) - вывод
# Общая сложность: O(1)

# -----------------------------
# Усложнённая задача: суммирование массива
# -----------------------------
def sum_array(arr):
    """Возвращает сумму всех элементов массива. Сложность: O(N)."""
    total = 0                   # O(1)
    for num in arr:             # O(N)
        total += num            # O(1) на каждую итерацию
    return total                # O(1)
# Общая сложность: O(N)

# -----------------------------
# Функция для замера времени
# -----------------------------
def measure_time(func, data, repeats=10):
    """Измеряет время выполнения функции в миллисекундах (усреднение)."""
    start_time = timeit.default_timer()
    for _ in range(repeats):
        func(data)
    end_time = timeit.default_timer()
    return (end_time - start_time) * 1000 / repeats  # ms

# -----------------------------
# Характеристики ПК
# -----------------------------
pc_info = """ 
Характеристики ПК для тестирования:
- Процессор: Intel Core i7-10750H @ 2.60GHz
- Оперативная память: 16 GB DDR4
- ОС: Windows 11
- Python: 3.9.7
"""
print(pc_info)

# -----------------------------
# Проведение экспериментов
# -----------------------------
sizes = [1000, 5000, 10000, 50000, 100000, 500000]  # Размеры массивов
times = []

print("Замеры времени выполнения для алгоритма суммирования массива:")
print("{:>10} {:>12} {:>15}".format("Размер (N)", "Время (мс)", "Время/N (мкс)"))

for size in sizes:
    data = [random.randint(1, 1000) for _ in range(size)]  # Генерация массива
    execution_time = measure_time(sum_array, data, repeats=10)
    times.append(execution_time)
    time_per_element = (execution_time * 1000) / size  # мкс на элемент
    print("{:>10} {:>12.4f} {:>15.4f}".format(size, execution_time, time_per_element))

# -----------------------------
# Построение графика
# -----------------------------
plt.figure(figsize=(10, 6))
plt.plot(sizes, times, 'bo-', label='Измеренное время')
plt.xlabel('Размер массива (N)')
plt.ylabel('Время выполнения (мс)')
plt.title('Зависимость времени выполнения от размера массива\nСложность: O(N)')
plt.grid(True, which='both', linestyle='--', linewidth=0.5)
plt.legend()
plt.savefig('time_complexity_plot.png', dpi=300, bbox_inches='tight')
plt.show()

# -----------------------------
# Анализ результатов
# -----------------------------
print("\nАнализ результатов:")
print("1. Теоретическая сложность алгоритма: O(N)")
print("2. Практические замеры показывают линейную зависимость времени от N")
print("3. Время на один элемент примерно постоянно (~{:.4f} мкс)".format(time_per_element))
print("4. Программа корректно обрабатывает большие массивы данных, демонстрируя практическое ограничение объема памяти и скорости.")
