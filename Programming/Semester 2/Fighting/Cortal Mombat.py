from random import randint, choices
import time

class Fighter:
    def __init__(self, name, age):
        self._Name = name
        self._Age = age
        self._crit_chance = 0.01
        self._attk_dmg = 20
        self._HP = 100
        self._replic_on_hit = 'Ударил'

    def get_replic_on_hit(self):
        return self._replic_on_hit

    def get_crit_chance(self):
        return self._crit_chance

    def set_crit_chance(self, chance):
        self._crit_chance = chance

    def get_name(self):
        return self._Name

    def set_name(self, name):
        self._Name = name

    def set_dmg(self, dmg):
        self._attk_dmg = dmg

    def get_dmg(self):
        return self._attk_dmg

    def set_HP(self, hp):
        self._HP = hp

    def get_HP(self):
        return self._HP

    def get_Age(self):
        return self._Age

    def __sub__(self, other):  # перегрузка вычитания
        name1 = self.get_name()
        name2 = other.get_name()
        new_style = self.get_Style()  # Стиль нового бойца = стилю уменьшаемого
        new_name = name1[:len(name1) // 2] + name2[len(name2) // 2:]  # Новое имя = половина первого + половина второго
        new_age = max(self.get_Age() - other.get_Age(), 1)  # Новый возраст
        new_HP = max(self.get_HP() - other.get_HP(), 1)  # Новое хп = разность хп двух бойцов
        new_dmg = max(self.get_dmg() - other.get_dmg(), 1)  # Новый урон = разность урона двух бойцов
        if new_style == 'Дзюдоист':  # Инициализация нового бойца
            new_fighter = Judo(new_name, new_age)
        else:
            new_fighter = Monk(new_name, new_age)
        new_fighter.set_HP(new_HP)
        new_fighter.set_dmg(new_dmg)
        return new_fighter

    def __add__(self, other): # перегрузка сложения
        name1 = self.get_name()
        name2 = other.get_name()
        new_style = self.get_Style() # Стиль нового бойца = стилю первого слагаемого
        new_name = name1[:len(name1)//2] + name2[len(name2)//2:] # Новое имя = половина первого + половина второго
        new_age = self.get_Age() + other.get_Age() # Новый возраст
        new_HP = self.get_HP() + other.get_HP() # Новое хп = сумма хп двух бойцов
        new_dmg = self.get_dmg() + other.get_dmg() # Новый урон = сумма урона двух бойцов
        if new_style == 'Дзюдоист': # Инициализация нового бойца
            new_fighter = Judo(new_name, new_age)
        else:
            new_fighter = Monk(new_name, new_age)
        new_fighter.set_HP(new_HP)
        new_fighter.set_dmg(new_dmg)
        return new_fighter




class Fight:
    def __init__(self):
        chosen_style1 = input('Выберите стиль бойца 1: Монах | Дзюдоист\n')
        chosen_name1 = input('Введите имя бойца 1: ')
        chosen_age1 = input('Введите возраст бойца 1: ') # Создание бойца 1
        try:
            chosen_age1 = int(chosen_age1)
        except:
            print('Вы неправильно ввели возраст, выбран стандартный возраст = 25 лет')
            chosen_age1 = 25
        if chosen_style1 == 'Монах':
            self.__player1 = Monk(chosen_name1, chosen_age1)
        elif chosen_style1 == 'Дзюдоист':
            self.__player1 = Judo(chosen_name1, chosen_age1)
        else:
            print(f'Вы неправильно ввели стиль. Выбран Дзюдоист.')
            self.__player1 = Judo(chosen_name1, chosen_age1)
        print('Боец 1 успешно создан')
        chosen_style2 = input('Выберите стиль бойца 2: Монах | Дзюдоист\n')
        chosen_name2 = input('Введите имя бойца 2: ')
        chosen_age2 = input('Введите возраст бойца 2: ') # Создание бойца 2
        try:
            chosen_age2 = int(chosen_age2)
        except:
            print('Вы неправильно ввели возраст, выбран стандартный возраст = 25 лет')
            chosen_age2 = 25
        if chosen_style2 == 'Монах':
            self.__player2 = Monk(chosen_name2, chosen_age2) # Инициализация бойца 1
        elif chosen_style2 == 'Дзюдоист':
            self.__player2 = Judo(chosen_name2, chosen_age2) # Инициализация бойца 2
        else:
            print(f'Вы неправильно ввели стиль. Выбран Дзюдоист.')
            self.__player2 = Judo(chosen_name2, chosen_age2)
        print('Боец 2 успешно создан')
    def Battle(self):
        player1, player2, turn_cnt = self.__player1, self.__player2, 0
        print(
            f"Добро пожаловать на Арену. Сегодня на ринге:\n\n В левом углу:"
            f" {player1.get_Style()} {player1.get_name()},"
            f" {player1.get_Age()} лет.\n\n В правом углу:"
            f" {player2.get_Style()} {player2.get_name()}, {player2.get_Age()} лет.\n\n Сражайтесь достойно.\n")
        players = [player1, player2] # Массив с бойцами
        replics = [player1.get_replic_on_hit(), player2.get_replic_on_hit()] # Массив с репликами
        names = [player1.get_name(), player2.get_name()] # Массив с именами бойцов
        time.sleep(2)
        while True:
            turn_cnt += 1
            turn = randint(0, 1)  # Выбираем, кто ходит рандомно
            print(f"---Ход {turn_cnt}---")
            print(f"Бьёт {players[turn].get_name()}!")
            print(f"{names[turn]} {replics[turn]} {names[1 - turn]}")
            dmg_raw = players[turn].get_dmg()  # Сила атаки бьющего
            crit_chance = players[turn].get_crit_chance()  # Шанс критического урона бьющего
            possible_damages = [dmg_raw, dmg_raw * 2]
            dmg = choices(possible_damages, [1 - crit_chance, crit_chance], k=1)[0]  # Роллим критический урон
            if dmg != dmg_raw:
                print("***КРИТИЧЕСКИЙ УРОН***")
            time.sleep(1)
            players[1 - turn].set_HP(players[1 - turn].get_HP() - dmg) # Уменьшаем здоровье бойца, которого ударили
            print(f"{names[1 - turn]} теряет {dmg} здоровья!")
            time.sleep(0.5)
            print(
                f"Здоровье кандидатов:\n {names[turn]}"
                f" {max(players[turn].get_HP(), 0)}\n {names[1 - turn]} {max(players[1 - turn].get_HP(), 0)}")
            if players[1 - turn].get_HP() <= 0:
                print(f"Победил {names[turn]}")
                break
            print()
            time.sleep(1)


class Judo(Fighter):
    def __init__(self, name, age):
        super().__init__(name, age)
        self._replic_on_hit = "дал в жбан"
        self._HP = 110
        self._style = 'Дзюдоист'

    def get_Style(self):
        return self._style

    def get_replic_on_hit(self):
        return self._replic_on_hit



class Monk(Fighter):
    def __init__(self, name, age):
        super().__init__(name, age)
        self._replic_on_hit = "ударил посохом по горбу"
        self._crit_chance = 0.05
        self._style = 'Монах'

    def get_crit_chance(self):
        return self._crit_chance

    def get_Style(self):
        return self._style

    def get_replic_on_hit(self):
        return self._replic_on_hit


fight = Fight()
fight.Battle()

