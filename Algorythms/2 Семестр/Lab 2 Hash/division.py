def hash_division(keys):
    n = len(keys)
    hash_table = [None for i in range(n)]
    for i in range(n):
        if hash_table[keys[i] % n] is None:
            hash_table[keys[i] % n] = [keys[i]]
        else:
            hash_table[keys[i] % n].append(keys[i])
    return hash_table

def display_hashtable(table):
    for i in range(len(table)):
        if table[i] is not None:
            print(i, '-->', *table[i])


keys = [11, 122, 123, 154, 15, 217, 108, 195, 124, 4, 1]

hash_table = hash_division(keys)
display_hashtable(hash_table)