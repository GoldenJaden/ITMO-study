n = 3
m = 5
profit = 0
stuff = [(1, 150), (10, 150), (5, 50), (4, 45), (10, 15), (5, 20)] # Ценные вещи: первый элемент - вес, второй - стоимость
stuff.sort(reverse=True, key=lambda tup: tup[1]) # Сортируем вещи по убыванию стоимости
stolen = [[] for i in range(n)] # Будем записывать украденные вещи в массив, индекс в массиве - номер ходки
current_bag = 0
while n != 0:
    k = 10
    i = 0
    while True:
        if len(stuff) != 0 and k - stuff[i][0] >= 0: # Если можно взять самую дорогую вещь - берём
            k -= stuff[i][0]
            profit += stuff[i][1]
            stolen[current_bag].append(stuff.pop(i))
        elif i < len(stuff) - 1: # Если нет - проверяем следующую
            i += 1
        else: # Ни одна вещь больше не влезает - идем на следующую ходку
            n -= 1
            current_bag += 1
            break

print(profit)
print(stolen)
print(stuff)
