import sqlite3

try:
    connection = sqlite3.connect('music.db')

    cursor = connection.cursor()
    print("База данных создана и успешно подключена к SQLite")

    select_query = "select sqlite_version();"
    cursor.execute(select_query)

    record = cursor.fetchall()
    print("Версия базы данных SQLite: ", record)

    cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
    tables = cursor.fetchall()

    if ("tMusician") not in tables:
        cursor.execute('''
            CREATE TABLE tMusician (
                id INTEGER PRIMARY KEY,
                canonicalName TEXT NOT NULL,
                age INTEGER NOT NULL,
                gender TEXT NOT NULL
            );
        ''')

        musicians = [
            ("Michael Jackson", 50, 'Male'),
            ("Eminem", 50, "Male"),
            ("Oxxxymiron", 38, "Male"),
            ("Taylor Swift", 33, "Female"),
            ("Billie Eilish", 21, "Female"),
            ("Dua Lipa", 27, "Female"),
            ("Selena Gomez", 30, "Female"),
            ("Elton John", 75, "Male"),
            ("Demi Lovato", 30, "Female"),
            ("Ariana Grande", 29, "Female")
        ]

        cursor.executemany("INSERT INTO tMusician(canonicalName, age, gender) VALUES(?, ?, ?)", musicians)

    if ("tSongs") not in tables:
        cursor.execute('''
            CREATE TABLE tSongs (
                id INTEGER PRIMARY KEY,
                id_musician INTEGER NOT NULL,
                title TEXT NOT NULL,
                description TEXT NOT NULL,
                FOREIGN KEY (id_musician) REFERENCES tMusician(id)
            );
        ''')

    songs = [
        (1, "Smooth criminal", "Legendary song"),
        (1, "Billie jean", "Moonwalk song"),
        (3, "Город под подошвой", "First song with production from oxxy"),
        (3, "Детектор лжи", "Good song"),
        (2, "Rap god", "Fast verse"),
        (4, "Shake it off", "Pop song"),
        (5, "Bad guy", "Catchy beat"),
        (6, "Don't start now", "Dance-pop song"),
        (7, "Lose you to love me", "Pop ballad about heartbreak"),
        (8, "Rocket man", "Classic rock ballad about an astronaut"),
        (9, "Sorry not sorry", "An upbeat pop song"),
        (10, "Thank U, Next", "Pop song about being grateful for past relationships")
    ]

    cursor.executemany("INSERT INTO tSongs(id_musician, title, description) VALUES(?, ?, ?)", songs)


    if ("tComments") not in tables:
        cursor.execute('''
            CREATE TABLE tComments (
                id INTEGER PRIMARY KEY,
                id_Musician INTEGER NOT NULL,
                id_Song INTEGER NOT NULL,
                textComm TEXT NOT NULL,
                FOREIGN KEY (id_Musician) REFERENCES tMusician(id),
                FOREIGN KEY (id_Song) REFERENCES tSongs(id)
            );
        ''')

        comments = [
            (1, 2, "My favorite song"),
            (1, 1, "My second favorite song"),
            (2, 1, "Good song"),
            (3, 4, "Fantastic"),
            (4, 5, "Awful"),
            (5, 10, "Great. Just great."),
            (6, 9, "A masterpiece"),
            (7, 8, "Dislike"),
            (8, 8, "Like"),
            (9, 1, "Boomer song"),
            (10, 2, "billie jean")
        ]

        cursor.executemany("INSERT INTO tComments(id_Musician, id_Song, textComm) VALUES(?, ?, ?)", comments)

    cursor.execute('SELECT * FROM tMusician')
    print('fetchall:', cursor.fetchall())
    cursor.execute('SELECT * FROM tSongs')
    print('fetchall:', cursor.fetchall())
    cursor.execute('SELECT * FROM tComments')
    print('fetchall:', cursor.fetchall())

    cursor.close()
except sqlite3.Error as error:
    print("Ошибка при подключении к sqlite", error)
finally:
    if (connection):
        connection.commit()
        connection.close()
        print("Соединение с SQLite закрыто")