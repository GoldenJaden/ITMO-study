def build_hash_table_div(inpt_str: str) -> list:
    keys = list(set(inpt_str)) # Все символы, встречающиеся в нашей строке
    n = len(keys)
    while True: # Ищем первое простое число, больше длины входных данных, чтобы уменьшить вероятность коллизии
        found = True
        for i in range(2, int(n ** 0.5 + 1)):
            if n % i == 0:
                found = False
                break
        if found == True:
            break
        n += 1
    hash_table = [None for i in range(n)]
    for s in keys: # Заполняем таблицу
        if hash_table[ord(s) % n] is None:
            hash_table[ord(s) % n] = [s]
        else:
            hash_table[ord(s) % n].append(s)
    return hash_table

in_str = "Hello world"
hashed_table = build_hash_table_div(in_str)
print(hashed_table)