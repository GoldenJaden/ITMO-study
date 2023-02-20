def kmp_count_substring(string, substring):
    n = len(string)
    m = len(substring)

    pi = [0] * m
    k = 0
    for i in range(1, m):
        while k > 0 and substring[k] != substring[i]:
            k = pi[k-1]
        if substring[k] == substring[i]:
            k += 1
        pi[i] = k

    count = 0
    k = 0
    for i in range(n):
        while k > 0 and substring[k] != string[i]:
            k = pi[k-1]
        if substring[k] == string[i]:
            k += 1
        if k == m:
            count += 1
            k = pi[k-1]

    return count