a = [76, -2, 75, 60, 5, 87, 41, 33, 81, 32, 70, -43, 21, -59, -68]
suma = 0
umn = 1
umn_kv = 1
for i in range(len(a)):
    suma += a[i]
for i in range(len(a)):
    umn *= a[i]
for i in range(len(a)):
    umn_kv *= a[i]**2
print(suma, umn, umn_kv)
