def naive(text: str, pattern: str) -> int:
    cnt = 0
    for i in range(len(text)-len(pattern)+1):
        if pattern == text[i:i+len(pattern)]:
            cnt += 1
    return cnt

example1 = 'ЭТОИЭТОТОТ'
template1 = 'ТОТО'
print(naive(example1, template1))
