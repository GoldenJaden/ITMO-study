import sqlite3

try:
    connection = sqlite3.connect('country.db')

    cursor = connection.cursor()
    print("База данных создана и успешно подключена к SQLite")

    select_query = "select sqlite_version();"
    cursor.execute(select_query)

    record = cursor.fetchall()
    print("Версия базы данных SQLite: ", record)

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")

    tables = cursor.fetchall()

    if ('CountriesTable',) not in tables:
        cursor.execute('''
            CREATE TABLE CountriesTable (
                id INTEGER PRIMARY KEY,
                name TEXT NOT NULL
            );
        ''')
        countries = [
            ('Украина',),
            ('Молдова',),
            ('Хорватия',),
            ('Египет',),
            ('Италия',),
            ('Индонезия',),
            ('Индия',),
            ('Чехословакия',),
            ('Америка',),
            ('Мексика',)
        ]

        cursor.executemany('INSERT INTO CountriesTable(name) VALUES (?)', countries)

    cursor.execute('SELECT * FROM CountriesTable')
    print('fetchall:', cursor.fetchall())

    cursor.close()
except sqlite3.Error as error:
    print("Ошибка при подключении к sqlite", error)
finally:
    if (connection):
        connection.commit()
        connection.close()
        print("Соединение с SQLite закрыто")