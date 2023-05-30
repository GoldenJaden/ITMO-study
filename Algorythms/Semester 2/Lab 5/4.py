def task(n):
    if n == 0 or n == 1:
        return 1
    if n == 2:
        return 2
    return task(n - 1) + task(n - 2) + task(n - 3)

print(task(10))