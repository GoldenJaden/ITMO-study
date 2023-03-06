text = 'Hello world'


def crc32(str_input: str) -> str:
    msg = ''
    for s in str_input:  # Проходимся по каждому символу в строке
        msg += bin(ord(s))[2:]  # Преобразуем символ в его ASCII-код, затем в двоичный вид и добавляем к msg

    g = '100110000010001110110110111'  # Задаем полином-генератор CRC32 в двоичном виде
    msg = msg + '0' * (len(g) - 1)  # Добавляем (len(g) - 1) нулей к msg

    block = msg[0:len(g)]  # Инициализируем первый блок первыми (len(g)) битами сообщения
    print(msg, block)
    i = len(g) - 1

    # Пока i меньше длины сообщения, выполняем XOR блока с полиномом-генератором
    while i < len(msg):
        block = bin(int(block, 2) ^ int(g, 2))[2:]

        # Если блок короче полинома-генератора, добавляем следующий бит сообщения к блоку
        while len(block) < len(g):
            i += 1
            if i < len(msg):
                block += msg[i]
            else:
                # Если мы достигли конца сообщения, возвращаем хеш CRC32 в шестнадцатеричном виде
                return hex(int(block, 2))

# Вызываем функцию crc32 для переменной text и печатаем результат
print(crc32(text))
