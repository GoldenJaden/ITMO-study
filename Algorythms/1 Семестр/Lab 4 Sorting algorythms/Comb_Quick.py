from combSort import combsort
from quickSort import quicksort

ex = [-82, -96, -46, 97, 95, 86, 44, -93, 31, -33, -9, 96, 8, 56, 72, 51, -67, -12, 55,
      26, 29, 67, 80, -90, -11, -2, -43, -73, -73, -7, 47, -91, 45, -94, 88, 65, -67, 99, 95, -2, 17]
method = input('Выберите метод сортировки (quick | comb) ')
#print('Далее введите ваш массив для сортировки через пробел')
#given = list(map(int, input().split()))
given = ex
if method == 'quick':
    print(quicksort(given, 0, len(given) - 1))
else:
    print(combsort(given))

import timeit
from random import randint as r
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib
matplotlib.style.use('ggplot')

def bucketsort(given):
    blocks = [[] for i in range((max(given) - min(given)) // 10 + 1)]
    negative_blocks = [[] for i in range((max(given) - min(given)) // 10)]
    for i in range(len(given)):
        if given[i] >= 0:
            blocks[given[i] // 10].append(given[i])
        else:
            negative_blocks[given[i] // 10].append(given[i])
    blocks = negative_blocks + blocks
    blocks = [sorted(elem) for elem in blocks]
    return [item for sublist in blocks for item in sublist]

def moveDown(Given, start, end):
    largest = 2 * start + 1
    while largest <= end:
        r = largest + 1
        if (largest < end) and (Given[largest] < Given[r]): # if right child > largest
            largest = r
        if Given[largest] > Given[start]: # if right child > root
            Given[largest], Given[start] = Given[start], Given[largest]
            start = largest;
            largest = 2 * start + 1
        else:
            return

def heapSort( Given ):
  length = len( Given ) - 1 # convert to heap
  leastParent = length // 2
  for i in range ( leastParent, -1, -1 ):
    moveDown( Given, i, length )


res = pd.DataFrame(
    index=['combsort', 'heapSort', 'quicksort', 'bucketsort'],
    columns=np.logspace(2, 3.5, 50).astype(int),
    dtype=float
)

for j in res.columns:
    b = [r(r(-50*j, -1000), r(1000, 50*j)) for i in range(j)]
    for i in res.index:
        a = b.copy()
        if i == 'quicksort':
            stmt = '{}(a, 0, len(a) - 1)'.format(i)
            setp = 'from __main__ import a, {}'.format(i)
            print('processing [{}]\tarray size: {}'.format(i, j), end='')
            res.at[i, j] = timeit.timeit(stmt, setp, number=10)
            print('\t\ttiming:\t{}'.format(res.at[i, j]))
        else:
            stmt = '{}(a)'.format(i)
            setp = 'from __main__ import a, {}'.format(i)
            print('processing [{}]\tarray size: {}'.format(i,j), end='')
            res.at[i, j] = timeit.timeit(stmt, setp, number=10)
            print('\t\ttiming:\t{}'.format(res.at[i, j]))
print(res)
plt.figure()
ax = res.T.plot(figsize=(10,8))
ax.set_xlabel('array size')
ax.set_ylabel('time (sec)')
plt.savefig('C:/Users/GoldenJaden/Desktop/result.png')
