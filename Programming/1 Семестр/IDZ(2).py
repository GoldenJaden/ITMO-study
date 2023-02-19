import datetime
from prettytable import PrettyTable

catalog = []

names = []

basket = []
purchased = []
last_id = 2542

def SaveCatalog(catal):
    f = open("Catalog.txt", 'w')
    for i in range(len(catal)):
        f.write(
            str(catal[i].get('Category')) + ' ' + str(catal[i].get('Price')) + ' ' + str(catal[i].get('Name')) + '\n')
    print('Список успешно сохранён')
    f.close()

def AddCatalog():
    global price, name, category
    print('Введите наименование, категорию и цену товара через пробел: \n')
    try:
        name, category, price = input().split()
    except:
        print('Неверный формат данных, попробуйте ещё раз')
        AddCatalog()
    while not(price.isdigit() and price != '0'):
        price = input("Неверный формат данных, введите корректную цену: ")
    while ' ' in name:
        name = input("Пожалуйста, вводите название без пробелов \n")
    catalog.append({'Category': category, 'Price': int(price), 'Name': name})
    names.append(name)
    print(f'Товар {name} успешно добавлен в каталог!')

def OpenCatalog():
    f = open("Catalog.txt", 'r')
    for s in f:
        category, price, nm = s.split()
        catalog.append({'Category': category, 'Price': int(price), 'Name': nm})
        names.append(nm)
    print('Каталог открыт')
    f.close()


def SavePurchased(pur):
    f = open("Purchased.txt", 'w')
    for i in range(len(pur)):
        f.write(str(pur[i][0]) + ' ' + str(pur[i][1]) + ' ' + str(pur[i][2]) + ' ' + str(pur[i][3]) + ' ' + str(pur[i][4]) + '\n')
    print('Список успешно сохранён')
    f.close()

def OpenPurchased():
    f = open("Purchased.txt", 'r')
    ids = []
    for s in f:
        pos1, pos2, pos3, pos4, pos5 = s.split()
        ids.append(int(pos1))
        purchased.append([int(pos1), pos2, int(pos3), pos4, pos5])
    global last_id
    last_id = max(ids)
    print('Список покупок успешно открыт')
    f.close()


OpenCatalog()
OpenPurchased()


def CheckList(bask):
    if len(bask) == 0:
        print('Список пуст')
    else:
        table = PrettyTable(['Название', 'Цена', 'Категория'])
        for i in range(len(bask)):
            table.add_row([bask[i].get('Name'), bask[i].get('Price'), bask[i].get('Category')])
        print(table)


def ShowPurchases(Pur):
    if len(Pur) == 0:
        print('Список пуст')
    else:
        table = PrettyTable(['id', 'Название', 'Цена', 'Категория', 'Дата покупки'])
        for i in range(len(Pur)):
            table.add_row([Pur[i][0], Pur[i][1], Pur[i][2], Pur[i][4], Pur[i][3]])
        print(table)


def help():
    print(
        '\n c_add - Добавить товар в каталог \n c_watch - Просмотреть каталог \n c_save - Сохранить каталог в файл \n price - Узнать цену товара \n'
        ' shopping - Начать заполнять корзину \n basket - Просмотреть корзину \n buy - Купить товары в корзине \n'
        ' p - Просмотреть записи о покупках \n p_save - Сохранить список покупок в файл \n help - Посмотреть список команд \n Чтобы закончить работу с программой введите Q \n')

print('HELP')
help()
while True:
    action = input()
    match action:
        case 'p_save':
            SavePurchased(purchased)

        case 'c_add':
            AddCatalog()

        case 'c_watch':
            CheckList(catalog)

        case 'c_save':
            SaveCatalog(catalog)
            print('Файл сохранён')

        case 'price':
            name = input('Введите название товара: \n')
            if name not in names:
                print('Такого товара нет в нашем магазине :(')
            else:
                print(f'Стоимость товара: {catalog[names.index(name)].get("Price")}')

        case 'shopping':
            print(
                'Вписывайте товары которые хотели бы добавить в корзину. Если хотите прекратить, введите "Q", если хотите просмотреть текущую корзину, введите "W", посмотреть каталог - "check"')
            while True:
                item = input()
                if item == 'Q':
                    print('Возвращаю вас на главный экран')
                    break
                elif item == 'W':
                    CheckList(basket)
                elif item == 'check':
                    CheckList(catalog)
                elif item not in names:
                    print('Такого товара нет в нашем магазине :(.')
                else:
                    basket.append(catalog[names.index(item)])

        case 'basket':
            CheckList(basket)

        case 'buy':
            if len(basket) == 0:
                print('Ваша корзина пуста')
            else:
                CheckList(basket)
                choice = input('Вы хотите совершить покупку? Yes/No \n')
                while choice not in ['Yes', 'No']:
                    choice = input('Введите Yes или No \n')
                if choice == 'Yes':
                    cost = 0
                    for i in range(len(basket)):
                        purchased.append(
                            [last_id + 1, basket[i].get('Name'), basket[i].get('Price'), str(datetime.date.today()),
                             basket[i].get('Category')])
                        last_id += 1
                    basket = []
                    print('Покупка совершена!')
                elif choice == 'No':
                    print('Возвращаю вас на главный экран')

        case 'p':
            new_purchased = purchased.copy()
            while True:
                choice = input('Выберите что хотите сделать: Посмотреть все покупки (all), '
                               'смотреть покупки по дате (d), смотреть покупки по категории (cat), сортировать по возрастанию цены (up) / убыванию цены (down) , удалить покупку (del) \n')
                if choice == 'all':
                    new_purchased = purchased.copy()
                    ShowPurchases(new_purchased)
                elif choice == 'd':
                    needed_date = input('Введите нужную дату в формате гггг-мм-дд: ')
                    new_purchased = [purchased[i] for i in range(len(purchased)) if purchased[i][3] == needed_date]
                    ShowPurchases(new_purchased)
                elif choice == 'cat':
                    needed_category = input('Выберите нужную категорию \n')
                    new_purchased = [purchased[i] for i in range(len(purchased)) if purchased[i][4] == needed_category]
                    ShowPurchases(new_purchased)
                elif choice == 'up':
                    new_purchased = sorted(new_purchased, key=lambda x: x[2])
                    ShowPurchases(new_purchased)
                elif choice == 'down':
                    new_purchased = sorted(new_purchased, key=lambda x: x[2], reverse=True)
                    ShowPurchases(new_purchased)
                elif choice == 'del':
                    num_to_del = int(input('Введите id записи, которую вы хотели бы удалить: \n'))
                    if num_to_del <= len(purchased) + 2542:
                        for i in range(len(purchased)):
                            if purchased[i][0] == num_to_del:
                                del purchased[i]
                                break
                elif choice == 'Q':
                    break
        case 'help':
            help()

        case 'Q':
            break
