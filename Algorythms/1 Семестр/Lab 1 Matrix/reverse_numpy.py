import numpy as np
import time
import timeit
# print('Далее введите по очереди каждую строчку матрицы (элементы матрицы разделены пробелом)')
# mat = [[0] * 3 for i in range(3)]
# for i in range(3):
#     mat[i] = list(map(int, input().split()))
# mat = np.array(mat)
# mat_reversed = np.linalg.inv(mat)
# print(mat_reversed)
print(timeit.timeit(stmt='np.linalg.inv(np.array([[1,2,3],[4,4,6],[7,8,9]]))', setup='import numpy as np', number=1))