from random import *


n = 100
N = [randint(-100, 100) for i in range(n)]
res = []
cur = 1
for i in range(n - 1):
    if N[i] < N[i+1]:
        cur += 1
    else:
        if cur > len(res):
            res = N[i - cur + 1: i]
        cur = 1
print(res)