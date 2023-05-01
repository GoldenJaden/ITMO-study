print('Далее введите по очереди каждую строчку матрицы (элементы матрицы разделены пробелом)')
mat = [[0] * 3 for i in range(3)]
for i in range(3):
    mat[i] = list(map(int, input().split()))
def reverse_mat(mat):
    def transp(mat):
        mat_transp = [[0] * 3 for i in range(3)]
        for i in range(3):
            for j in range(3):
                mat_transp[j][i] = mat[i][j]
        return mat_transp
    det_mat = (mat[0][0] * (mat[1][1]*mat[2][2] - mat[1][2]*mat[2][1]))\
        - (mat[0][1]*(mat[1][0]*mat[2][2] - mat[1][2]*mat[2][0]))\
        + (mat[0][2]*(mat[1][0]*mat[2][1] - mat[2][0]*mat[1][1]))               # Находим детерминанту
    if det_mat == 0:
        print('Определитель равен нулю. Обратую матрицу вычислить невозможно.')
    else:
        reverse_mat = [[0]*3 for i in range(3)]
        opr = transp(mat)
        for i in range(3):
            for j in range(3):
                opr.pop(i)                                                  # Ищем миноры
                for p in range(2):
                    del opr[p][j]
                reverse_mat[i][j] = '{0:g}'.format(round(float((-1)**(i+j) * (opr[0][0]*opr[1][1] - opr[0][1]*opr[1][0]) / det_mat), 2))
                opr = transp(mat)
        return reverse_mat
j = reverse_mat(mat)
print('Обратная матрица:')
for i in range(3):
    print(*j[i])


