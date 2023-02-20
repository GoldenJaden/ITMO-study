def hash(stroka: str, alphabet) -> int:
    h = 0
    x = len(alphabet)
    stroka = stroka[::-1]
    m = len(stroka)
    for i in range(m):
        h += int(list(alphabet).index(stroka[i]))*x**(i)
    return h

def karp(text: str, pattern: str) -> int:
    alphabet = list(set(text))
    cnt = 0
    hash_template = hash(pattern, alphabet)
    for i in range(len(text) - len(pattern)+1):
        if hash_template == hash(text[i:i+len(pattern)], alphabet):
            if pattern == text[i:i+len(pattern)]:
                cnt += 1
    return cnt

example1 = 'abcaabkab'
template1 = 'ab'
print(karp(example1, template1))



