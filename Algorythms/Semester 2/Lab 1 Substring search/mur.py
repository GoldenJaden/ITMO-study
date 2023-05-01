def mur(example: str, pattern: str) -> int:
    if len(pattern) == 0 or len(example) == 0:
        return 0
    offsets = [None for i in range(len(pattern))]
    cnt = 0
    pb = pattern[::-1]
    for i in range(1, len(pattern) + 1):  # filling the offset list
        compl = (pb[1:] + pb[0])[:i - 1]
        j = pb[i % len(pb)]
        if pb[i % len(pb)] not in compl:
            offsets[i % len(pattern)] = i
        else:
            offsets[i % len(pattern)] = compl.index(pb[i % len(pb)]) + 1
    offsets = offsets[::-1]
    offsets.append(len(pattern))
    p = len(pattern) - 1
    while p < len(example):  # the main algorythm
        j = len(pattern) - 1
        while j >= 0:
            if p >= len(example):
                break
            if pattern[j] != example[p]:
                j = len(pattern) - 1
                if example[p] in pattern:
                    p += offsets[pattern.index(example[p])]
                else:
                    p += offsets[-1]
            else:
                j, p = j - 1, p - 1
        if j == -1:
            cnt += 1
            p += 2 * offsets[-1]
        else:
            j = len(pattern) - 1
    return cnt


example1 = 'abcaabkab'
template1 = 'ab'
print(mur(example1, template1))

# ВРОДЕ ПОФИКСИЛ
