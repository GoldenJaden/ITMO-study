import numpy as num

n = 5 #кол-во экспонатов
w = 13 #вес, который вор унесет за раз
m = 2 #количество заходов

exp_w = [3, 4, 5, 8, 9] #вес каждого экспоната
exp_p = [1, 6, 4, 7, 6] #стоимость каждого экспоната

ans = 0

def func(n, w):
    a = num.zeros((n, w)): #двумерный массив с промежуточными результатами
    global exp_w
    global exp_p
    for k in range(n):
        for s in range(w):
            if s >= exp_w[k]: #проверяем помещается предмет в рюкзак или нет
                a[k][s] = max(a[k-1][s], a[k-1][s - exp_w[k]] + exp_p[k])#если да, то кладем
            else:
                a[k][s] = a[k-1][s]
    ans = a[n-1][w-1]
    sum = a[n-1][w-1]
    j = w-1
    for i in range(n-1, 0, -1):#идем от обратного и убираем из списка, далее вызываем с новыми значениеями
        if sum == 0:
            break
        if a[i-1][j] != sum:
            j -= exp_p[i]
            n -= 1
            exp_w.remove(exp_w[i])
            exp_w.remove(exp_p[i])
    return ans, n

for i in range(m):
    tek, n = func(n, w)
    ans += tek
print(ans)