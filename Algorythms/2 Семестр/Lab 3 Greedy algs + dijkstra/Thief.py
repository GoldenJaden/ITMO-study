n = 4 # количество экспонатов
m = 2 # количество заходов
profit = 0
stuff = [(10, 150), (10, 150), (1, 100), (4, 45), (10, 15), (5, 20)] # Ценные вещи: первый элемент - вес, второй - стоимость
stuff.sort(reverse=True, key=lambda tup: tup[1]) # Сортируем вещи по убыванию стоимости
stolen = [[] for i in range(n)] # Будем записывать украденные вещи в массив, индекс в массиве - номер ходки
current_bag = 0
while m != 0:
    enough = False
    k = 10
    i = 0
    while True:
        if n == 0:
            enough = True
            break
        if len(stuff) != 0 and k - stuff[i][0] >= 0: # Если можно взять самую дорогую вещь - берём
            k -= stuff[i][0]
            profit += stuff[i][1]
            n -= 1
            stolen[current_bag].append(stuff.pop(i))
        elif i < len(stuff) - 1: # Если нет - проверяем следующую
            i += 1
        else: # Ни одна вещь больше не влезает - идем на следующую ходку
            m -= 1
            current_bag += 1
            break
    if enough:
        break

print(f'Сумма украденного: {profit}')
print('Украденные вещи:', end=" ")
print(*filter(None, stolen))
print('Оставшиеся вещи:', end=" ")
print(*stuff)
