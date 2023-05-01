a = [-74, -68, -62, -59, -43, -30, -22, -13]
for i in range(len(a)-1, -1, -1):
    x = a[i]
    mx = len(a)
    mn = 0
    mid = (mx + mn) // 2
    while a[mid] != x:
        if a[mid] < x:
            mn = mid
        elif a[mid] > x:
            mx = mid
        mid = (mx + mn) // 2
    print(a[mid])
