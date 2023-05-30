import numpy as np

matrix = [[-97, -85, -67, -65, -50, -33, 13, 20, 43, 86],
        [-88, -78, -67, -55, -48, 1, 15, 28, 55, 89],
        [-87, -73, -61, -37, -20, 14, 21, 40, 59, 95],
        [-86, -71, -43, -29, -6, 14, 41, 49, 74, 98],
        [-79, -60, -31, 3, 18, 27, 44, 55, 86, 98]]


def search(elem, arr):
    n = len(arr)  # количество строк
    m = len(arr[0])  # количество столбцов

    # Правый верхний угол матрицы
    i = 0
    j = m - 1

    while i < n and j >= 0:
        if arr[i][j] == elem:
            return (f'Ряд: {i + 1}', f'Столбец: {j + 1}')
        elif arr[i][j] < elem:
            i += 1
        else:
            j -= 1

    return "Элемент не найден"


print(search(-20, matrix))

# Сложность O(nlogm), где n - кол-во строк, m - колво столбцов матрицы