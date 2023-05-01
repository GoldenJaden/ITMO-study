from random import randint as r

a = [-74, -68, -62, -59, -43, -30, -22, -13]
for i in range(3):
    x = a[r(0, len(a))-1]
    print(f'Ищем {x}')
    mx = len(a)
    mn = 0
    mid = (mx + mn) // 2
    while a[mid] != x:
        if a[mid] < x:
            mn = mid
        elif a[mid] > x:
            mx = mid
        mid = (mx + mn) // 2
    print(a[mid], mid)
