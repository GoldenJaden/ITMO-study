import numpy as np
n, m = map(int, input('Введите размер матрицы в формате высота:ширина ').split(':'))
print('Далее введите по очереди каждую строчку матрицы (элементы матрицы разделены пробелом)')
mat = [[0] * m for i in range(n)]
for i in range(n):
    mat[i] = list(map(int, input().split()))
mat = np.array(mat)
action = input('Выберите действие: Транспонировать (Т), Умножить (У): ')
if action == 'Транспонировать' or action == 'Т':
    transposed_mat = mat.transpose()
    print('Ваша транспонированная матрица:')
    print(transposed_mat)
elif action == 'Умножить' or action == 'У':
    n2, m2 = map(int, input('Введите размер второй матрицы в формате высота:ширина ').split(':'))
    print('Далее введите по очереди каждую строчку матрицы (элементы матрицы разделены пробелом)')
    mat2 = [[0] * m2 for i in range(n2)]
    for i in range(n2):
        mat2[i] = list(map(int, input().split()))
    mat2 = np.array(mat2)
    mult_mat = np.matmul(mat, mat2)
    print('Ваше произведение:')
    print(mult_mat)
