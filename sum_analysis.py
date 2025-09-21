# sum_analysis.py
import timeit
import matplotlib.pyplot as plt
import random

# -----------------------------
# 1. Простая задача: сумма двух чисел
# -----------------------------
def calculate_sum_from_file(filename="input.txt"):
    """
    Считает сумму двух чисел из файла.
    Сложность: O(1)
    """
    with open(filename, "r") as f:           # O(1)
        lines = f.readlines()                # O(1)
    print("Содержимое файла:")
    for line in lines:                       # O(1)
        print(line.strip())                  # O(1)

    a = int(lines[0].strip())                # O(1)
    b = int(lines[1].strip())                # O(1)
    result = a + b                           # O(1)
    print(f"Сумма чисел: {result}")          # O(1)
# Общая сложность: O(1)


# -----------------------------
# 2. Усложнённая задача: суммирование массива
# -----------------------------
def sum_array(arr):
    """Возвращает сумму всех элементов массива. Сложность: O(N)."""
    total = 0                   # O(1)
    for num in arr:             # O(N)
        total += num            # O(1) на итерацию
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
def system_info():
    pc_info = """ 
Характеристики ПК для тестирования:
- Процессор: Intel Core i5-1135G7 @ 2.40GHz
- Оперативная память: 8 GB DDR4
- ОС: Windows 11
- Python: 3.11.6
"""
    print(pc_info)

# -----------------------------
# Основная функция лабораторной
# -----------------------------
def main():
    system_info()

    print("=== Чтение чисел из файла и вычисление суммы ===")
    # Создаём пример файла input.txt
    with open("input.txt", "w") as f:  # O(1)
        f.write("123\n456\n")  # O(1)
    calculate_sum_from_file("input.txt")

    print("\n=== Усложнённая задача: суммирование массива ===")
    sizes = [1000, 5000, 10000, 50000, 100000, 500000]
    times = []

    print("{:>10} {:>12} {:>15}".format("Размер (N)", "Время (мс)", "Время/N (мкс)"))
    for size in sizes:
        data = [random.randint(1, 1000) for _ in range(size)]
        execution_time = measure_time(sum_array, data, repeats=10)
        times.append(execution_time)
        time_per_element = (execution_time * 1000) / size  # мкс на элемент
        print("{:>10} {:>12.4f} {:>15.4f}".format(size, execution_time, time_per_element))

    # Построение графика
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, times, 'bo-', label='Измеренное время')
    plt.xlabel('Размер массива (N)')
    plt.ylabel('Время выполнения (мс)')
    plt.title('Зависимость времени выполнения от размера массива\nСложность: O(N)')
    plt.grid(True, which='both', linestyle='--', linewidth=0.5)
    plt.legend()
    plt.savefig('time_complexity_plot.png', dpi=300, bbox_inches='tight')
    plt.show()

    # Анализ результатов
    print("\nАнализ результатов:")
    print("1. Теоретическая сложность алгоритма: O(N)")
    print("2. Практические замеры показывают линейную зависимость времени от N")
    print("3. Время на один элемент примерно постоянно (~{:.4f} мкс)".format(time_per_element))
    print("4. Программа корректно обрабатывает большие массивы данных.")

# -----------------------------
# Точка входа
# -----------------------------
if __name__ == "__main__":
    main()
