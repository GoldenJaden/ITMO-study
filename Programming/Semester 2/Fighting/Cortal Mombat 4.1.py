from random import randint, choices
import time
from abc import ABC, abstractmethod
from threading import Thread

# Декораторы
def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(f"Время выполнения функции {func.__name__}: {format(end_time - start_time, '.2f')} секунд")
        return result
    return wrapper

# Исключения
class WrongAgeError(Exception):
    def __init__(self, age):
        self.age = age

    def __str__(self):
        return f'"{self.age}" является неверным возрастом. Обратите внимание, ' \
               f'что возраст может быть только положительным целым числом.'

class WrongStyleError(Exception):
    def __init__(self, style):
        self.style = style

    def __str__(self):
        return f'"{self.style}" является неверным стилем. Обратите внимание, ' \
               f'что вам нужно выбрать из двух стилей: Монах | Дзюдоист'


class hairColorMixin:
    def set_hairColor(self, color):
        self._hairColor = color

    def get_hairColor(self):
        return self._hairColor

class Human(hairColorMixin):
    def __init__(self, name, age):
        self._Name = name
        self._Age = age

    def get_age(self):
        return self._Age

    def get_name(self):
        return self._Name

    def set_name(self, name):
        self._Name = name


class Fighter(ABC, Human):
    def __init__(self, name, age):
        super().__init__(name, age)
        self._replic_on_hit = 'Ударил'
        self._Name = name
        self._Age = age
        self._crit_chance = 0.05
        self._attk_dmg = 20
        self._HP = 100
        self._dodge_chance = 0.05

    def get_replic_on_hit(self):
        return self._replic_on_hit

    def get_crit_chance(self):
        return self._crit_chance

    def get_dodge_chance(self):
        return self._dodge_chance

    def set_crit_chance(self, chance):
        self._crit_chance = chance

    def set_dmg(self, dmg):
        self._attk_dmg = dmg

    def get_dmg(self):
        return self._attk_dmg

    def set_HP(self, hp):
        self._HP = hp

    def get_HP(self):
        return self._HP

    @abstractmethod
    def get_attackReplic(self, name2): # Абстрактный метод, т.к у разных бойцов разные реплики
        pass

    @abstractmethod
    def get_style(self): # Абстрактный метод, т.к у разных бойцов разные стили
        pass

    def __sub__(self, other):  # перегрузка вычитания
        name1 = self.get_name()
        name2 = other.get_name()
        new_style = self.get_style()  # Стиль нового бойца = стилю уменьшаемого
        new_name = name1[:len(name1) // 2] + name2[len(name2) // 2:]  # Новое имя = половина первого + половина второго
        new_age = max(self.get_age() - other.get_age(), 1)  # Новый возраст
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
        new_style = self.get_style() # Стиль нового бойца = стилю первого слагаемого
        new_name = name1[:len(name1)//2] + name2[len(name2)//2:] # Новое имя = половина первого + половина второго
        new_age = self.get_age() + other.get_age() # Новый возраст
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

        # Создание бойца 1
        chosen_style = input('Выберите стиль бойца 1: Монах | Дзюдоист\n')
        chosen_name = input('Введите имя бойца 1: ')
        chosen_age = input('Введите возраст бойца 1: ')
        chosen_hairColor = input('Введите цвет волос бойца 1: ')
        #self.buildFighter(chosen_style, chosen_name, chosen_age, chosen_hairColor, "1")
        thread1 = Thread(target=self.buildFighter(chosen_style, chosen_name, chosen_age, chosen_hairColor, "1"))

        # Создание бойца 2
        chosen_style = input('Выберите стиль бойца 2: Монах | Дзюдоист\n')
        chosen_name = input('Введите имя бойца 2: ')
        chosen_age = input('Введите возраст бойца 2: ')
        chosen_hairColor = input('Введите цвет волос бойца 2: ')
        #self.buildFighter(chosen_style, chosen_name, chosen_age, chosen_hairColor, "2")
        thread2 = Thread(target=self.buildFighter(chosen_style, chosen_name, chosen_age, chosen_hairColor, "2"))

        self._turn_cnt = 0

        # Мультитрединг на создание бойцов
        thread1.start()
        thread2.start()
        thread1.join()
        thread2.join()

    '''
    def __init__(self):
        self._player1 = Monk('Монах', 100)
        self._player2 = Judo('Чун Ли', 25)
        self._turn_cnt = 0
    '''
    def buildFighter(self, style, name, age, hairColor, num):
        try:
            age = self.checkValidAge(age)
        except:
            print(
                "Введённый возраст не является верным. Обратите внимание,что возраст может быть только положительным целым числом. Выбран стандартный возраст: 25 лет")
            age = 25
        if style == 'Монах':
            setattr(self, "_player" + num, Monk(name, age))
            #self._player1 = Monk(name, age)
        elif style == 'Дзюдоист':
            setattr(self, "_player" + num, Judo(name, age))
            #self._player1 = Judo(name, age)
        else:
            try:
                self.checkValidStyle(style)
            except:
                print(f'Вы ввели несуществующий стиль. Выбран стандартный стиль: Дзюдоист.')
                setattr(self, "_player" + num, Judo(name, age))
                #self._player1 = Judo(name, age)
        if num == "1":
            self._player1.set_hairColor(hairColor)
        else:
            self._player2.set_hairColor(hairColor)
        print(f'Боец {name} успешно создан')

    def checkValidAge(self, age):
        if age.isdecimal() and int(age) != 0:
            return int(age)
        else:
            raise WrongAgeError(age)

    def checkValidStyle(self, style):
        if style not in ['Дзюдоист', 'Монах']:
            raise WrongStyleError(style)
        else:
            return True

    # Геттеры, сеттеры
    def getPlayers(self):
        return [self._player1, self._player2]

    # Роллы
    def critRoll(self):
        players = self.getPlayers()
        dmg_raw = players[self._turn].get_dmg()  # Сила атаки бьющего
        crit_chance = players[self._turn].get_crit_chance()  # Шанс критического урона бьющего
        possible_damages = [dmg_raw, dmg_raw * 2]
        dmg = choices(possible_damages, [1 - crit_chance, crit_chance], k=1)[0]  # Роллим критический урон
        if dmg != dmg_raw:
            print("***КРИТИЧЕСКИЙ УРОН***")
        return dmg

    def dodgeRoll(self):
        players = self.getPlayers()
        dodge_chance = players[1 - self._turn].get_dodge_chance()
        isDodged = choices([False, True], [1 - dodge_chance, dodge_chance], k=1)[0]
        return isDodged

    # Уменьшение здоровья
    def reduceHealth(self, dmg):
        players = self.getPlayers()
        players[1 - self._turn].set_HP(players[1 - self._turn].get_HP() - dmg)  # Уменьшаем здоровье бойца, которого ударили
        print(f"{players[1 - self._turn].get_name()} теряет {dmg} здоровья!")

    # Реплики
    def greetingsReplic(self):
        players = self.getPlayers()
        print(
            f"Добро пожаловать на Арену. Сегодня на ринге:\n\n В левом углу:"
            f" {players[0].get_style()} {players[0].get_name()},"
            f" {players[0].get_age()} лет, цвет волос: {players[0].get_hairColor()}.\n\n В правом углу:"
            f" {players[1].get_style()} {players[1].get_name()}, {players[1].get_age()} лет, цвет волос: {players[1].get_hairColor()}.\n\n Сражайтесь достойно.\n")

    def startMoveReplic(self):
        players = self.getPlayers()
        print(f"---Ход {self._turn_cnt}---")
        print(f"Бьёт {players[self._turn].get_name()}!")
        print(players[self._turn].get_attackReplic(players[1 - self._turn].get_name()))  # Удар

    def remain_health(self):
        players = self.getPlayers()
        print(
            f"Здоровье кандидатов:\n {players[self._turn].get_name()}"
            f" {max(players[self._turn].get_HP(), 0)}\n {players[1 - self._turn].get_name()} {max(players[1 - self._turn].get_HP(), 0)}")

    # Ход
    def move(self):
        players = self.getPlayers()
        self._turn_cnt += 1
        self._turn = randint(0, 1)  # Выбираем, кто ходит рандомно
        self.startMoveReplic()
        time.sleep(1)
        print()
        if not self.dodgeRoll():
            dmg = self.critRoll()
            self.reduceHealth(dmg)
        else:
            print(f'___{players[1 - self._turn].get_name()} увернулся!___')
        time.sleep(0.5)
        print()
        self.remain_health()
        if players[1 - self._turn].get_HP() <= 0:
            print()
            print(f"Победил {players[self._turn].get_name()}")
            return 0
        print()
        time.sleep(1)
        return 'continue'

    @timer
    def Battle(self):
        self.greetingsReplic()
        while True:
            time.sleep(1)
            move_result = self.move()
            if move_result == 0:
                break

class Judo(Fighter):
    def __init__(self, name, age):
        super().__init__(name, age)
        self._replic_on_hit = "дал в жбан"
        self._HP = 110
        self._style = 'Дзюдоист'
        self._dodge_chance = 0.1

    def get_style(self):
        return self._style

    def get_attackReplic(self, name2):
        return f"{self.get_name()} {self.get_replic_on_hit()} {name2}"


class Monk(Fighter):
    def __init__(self, name, age):
        super().__init__(name, age)
        self._replic_on_hit = "ударил посохом по горбу"
        self._crit_chance = 0.1
        self._style = 'Монах'

    def get_style(self):
        return self._style

    def get_attackReplic(self, name2):
        return f"{self.get_name()} {self.get_replic_on_hit()} {name2}"






fight = Fight()
fight.Battle()

'''
Условности игры:
Критические шансы:
1) Монах 5 %
2) Дзюдоист 1%

Накапливается ярость, если критические удары бла бла бла..
'''