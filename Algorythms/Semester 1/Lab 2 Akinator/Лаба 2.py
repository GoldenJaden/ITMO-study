from random import *

def restart():
    answer = input('Хотите сыграть ещё раз? (Д/Н): ')
    if answer == 'Д':
        global questions_inGame, students_char_inGame, tags
        questions_inGame = questions.copy()
        students_char_inGame = students_char.copy()
        tags = tags_save.copy()
    else:
        print('Конец игры')
        return 0

students_char = {"Агаев Хамза":['М','Чай','Кофе','Чёрные','Кошки'], "Николай Ершов":['М','Водила','Кошки','Каштановые'], 'Надежда Цветкова':['Ж','Чай','Кофе','Спортик','Собаки'], 'Яна Морозова':['Ж','Чай','Кошки'],
                 'Алиса Коломиец':['М'], 'Александра Шимченко':['Ж','Чай','Кошки','Кофе','Собаки'], 'Роман Мордовцев':['М','Чай','Кошки','Кофе','Собаки','Светлые'], 'Патина Гаджиева':['Ж'],
                 'Ярослав Гусев(Я)':['М','Чай','Кофе','Собаки','Кошки','Спортик','Алкаш','Чёрные'], 'Матвей Морозов':['М','Чай','Собаки','Алкаш','Чёрные'], 'Амир Уразалин':['М','Кошки','Кофе','Собаки','Чёрные','ГР'],
                 'Савва Мамонтов':['М','Куряга','Чай','Кофе','Спортик','Собаки','Алкаш','Русые'], 'Иван Скворцов':['М','Чай','Кошки','Кофе'], 'Кристина Шевченко':['Ж','Чёрные','Собаки'], 'Анастасия Иванова':['Ж','Чай','Кошки'], 'Алексей Мартынюк':['М','Кошки','Кофе','Жонглёр'],
                 'Алина Фёдорова':['Ж','Чай','Кошки','Кофе','Спортик','Алкаш','Чёрные'], 'Мустафа Абдалла':['М','ГР','Чёрные','Кофе','Собаки'], 'Макс Гуренков':['М','Чай','Спортик','Куряга','Каштановые'], 'Миша Шапиро':['М','Кошки','Кофе','Спортик','Алкаш','Водила','Каштановые'],
                 'Рома Шабанов':['М','Светлые','Кофе','Собаки'], 'Дмитрий Сидненко':['М','Чай','Собаки'],
                 'Анастасия Бахтина':['Ж','Чай','Кофе','Кошки','Спортик','Собаки'],'Полина Колтунова':['Ж','Чай','Спортик','Каштановые'], 'Алексей Мыльченко':['М','Чай','Собаки','Алкаш'], 'Киро Эскандер':['М','ГР','Чёрные','Кофе','Собаки'], 'Олег Георгов':['М','Светлые','Русые','Чай','Собаки','Кошки'],
                 'Владимир Луценко':['М','Чай','Кошки'], 'Олег Якунин':['М'], 'Денис Мигулян':['М']}
students_char_inGame = students_char.copy()

tags = ['Ж', 'Чай', 'Кофе', 'Жонглёр', 'Водила', 'Спортик', 'ГР', 'Кошки', 'Собаки',
        'Алкаш', 'Куряга', 'Чёрные', 'Каштановые', 'Русые', 'Светлые']
tags_save = tags.copy()

questions = ['Студент студентка?', 'Студент любит чай?', 'Студент любит кофе?',
             'Студент умеет жонглировать?', 'Студент умеет водить машину?', 'Студент занимается спортом?',
             'Студент из-за границы?', 'Студент любит кошек?', 'Студент любит собак?', 'Студент пьёт алкоголь?',
             'Студент курит/парит?', 'У студента чёрные волосы?', 'У студента каштановые волосы?',
             'У студента русые волосы?', 'У студента светлые волосы?']
questions_inGame = questions.copy()
while True:
    print(len(students_char_inGame))
    if len(students_char_inGame) == 0:
        print('Я сдаюсь')
        if restart() == 0: break

    if len(students_char_inGame) == 1:
        print(f'Человек, которого вы загадали это: {list(students_char_inGame)[0]}')
        if restart() == 0: break

    question_number = randint(0, len(questions_inGame) - 1)
    question = questions_inGame[question_number]
    tag = tags[question_number]
    print(question)
    answer = input('Д/Н/ХЗ: ')
    students_char_inGame_otbor = dict()
    if answer == 'Д':
        for i in range(len(students_char_inGame)):
            if tag in students_char_inGame.get(list(students_char_inGame)[i]):
                students_char_inGame_otbor[list(students_char_inGame)[i]] = students_char_inGame[list(students_char_inGame)[i]]
        questions_inGame.remove(question)
        tags.remove(tag)
    elif answer == 'Н':
        for i in range(len(students_char_inGame)):
            if tag not in students_char_inGame.get(list(students_char_inGame)[i]):
                students_char_inGame_otbor[list(students_char_inGame)[i]] = students_char_inGame[list(students_char_inGame)[i]]
        questions_inGame.remove(question)
        tags.remove(tag)
    elif answer == 'ХЗ':
        continue
    students_char_inGame = students_char_inGame_otbor.copy()



