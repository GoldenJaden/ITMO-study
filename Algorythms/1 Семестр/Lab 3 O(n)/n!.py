n = int(input())
def factorials(n):
    if n <= 0: return 0
    k = 1
    for i in range(1, n + 1):
        k *= i
    print(k)
    factorials(n-1)
factorials(n)



