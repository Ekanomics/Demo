# 1 - Найдите и скопируйте алгоритм бинарного поиска. Запустите код и попробуйте разобраться как он работает

# Отсортированный массив
datalist = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]
# Значение, которое надо найти
value = 23

def бинарный_поиск(datalist, value):
    # границы поиска
    left = 0
    right = len(datalist) - 1

    while left <= right:
        # Находим средний индекс
        center = (left + right) // 2

        # Если средний элемент равен искомому значению, возвращаем его индекс
        if datalist[center] == value:
            return center

        # Если значение меньше среднего, перемещаем правую границу
        elif datalist[center] > value:
            right = center - 1

        # Если значение больше среднего, перемещаем левую границу
        else:
            left = center + 1

    # Если элемент не найден, возвращаем -1
    return -1


# Запускаем бинарный поиск
result = бинарный_поиск(datalist, value)

# Выводим результат
if result != -1:
    print("Значение " + str(value) + " найдено в индексе " + str(result))
else:
    print("Значение " + str(value) + " не найдено")








# 2 - Найдите и скопируйте алгоритм пузырьковой сортировки. Запустите код и попробуйте разобраться как он работает

data = [23, 33, 16, 77, 45, 95, 53, 65, 9, 82, 44, 66, 2]

def bubble_sort(data):
    # Длина массива
    n = len(data)

    # Проходим по всему массиву
    for i in range(n):
        # Для отслеживания, были ли изменения в этой итерации
        a = False

        # Сравниваем соседние элементы
        for j in range(0, n - i - 1):
            if data[j] > data[j + 1]:
                # Меняем элементы местами
                data[j], data[j + 1] = data[j + 1], data[j]
                a = True

        # Если в этой итерации не было изменений, массив отсортирован
        if not a:
            break

    return data


print("Unsorted data:", data)

Sorted_data = bubble_sort(data)
print("Sorted data:", Sorted_data)