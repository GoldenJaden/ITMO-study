n, m = map(int, input('Введите размер матрицы в формате высота:ширина ').split(':'))
print('Далее введите по очереди каждую строчку матрицы (элементы матрицы разделены пробелом)')
mat = [[0] * m for i in range(n)]
for i in range(n):
    mat[i] = list(map(int, input().split()))
def transp(mat, n, m):
    mat_transp = [[0] * n for i in range(m)]
    for i in range(n):
        for j in range(m):
            mat_transp[j][i] = mat[i][j]
    return mat_transp

def mult(mat, mat2):
    mult_mat = [[0] * m2 for i in range(n)]
    mat2 = transp(mat2, n2, m2)
    for i in range(n):
        for j in range(m2):
            for elem in range(n2):
                mult_mat[i][j] += mat[i][elem] * mat2[j][elem]
    return mult_mat

action = input('Выберите действие: Транспонировать (Т), Умножить (У): ')
if action == 'Транспонировать' or action == 'Т':
    mat_transp = transp(mat, n, m)
    print('Ваша транспонированная матрица:')
    for i in range(m):
        print(*mat_transp[i])
elif action == 'Умножить' or action == 'У':
    n2, m2 = map(int, input('Введите размер второй матрицы в формате высота:ширина ').split(':'))
    print('Далее введите по очереди каждую строчку матрицы (элементы матрицы разделены пробелом)')
    mat2 = [[0] * m2 for i in range(n2)]
    for i in range(n2):
        mat2[i] = list(map(int, input().split()))
    u = mult(mat, mat2)
    print('Ваше произведение:')
    for i in range(n):
        print(*u[i])
