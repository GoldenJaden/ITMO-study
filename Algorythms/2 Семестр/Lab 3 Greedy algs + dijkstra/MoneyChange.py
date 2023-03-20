M1 = 5
S1 = 5

M2 = 5
S2 = 2

M3 = 5
S3 = 1

M4 = 4
S4 = 10

N = 50 #сдача пользователю
res = []

a = [[S1, M1], [S2, M2], [S3, M3], [S4, M4]]
a.sort(reverse=True)

for i in range(len(a)):
    while (N-a[i][0] >= 0) and (a[i][1] != 0):
        N -= a[i][0]
        res.append(a[i][0])
        a[i][1] -= 1
print(res)
