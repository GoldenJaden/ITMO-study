arr = [1, 3, 5, 6, 2, 9, 8, 12, 11, 4, 7, 15, 14, 16, 10, 13, 17, 33, 20, 19, 21, 21, 18, 23, 22, 24, 26, 25, 27, 28, 29, 31, 32, 34]

# method 1
def find_hole(arr):
    s = set(arr)
    for i in range(1, len(arr)):
        if i not in s:
            return i
    return -1

# method 2
def find_hole_2(arr):
    map = [False for i in range(len(arr))]
    for i in range(1, len(arr)):
        if i in arr:
            map[i] = True
    if False in map[1:]:
        return map[1:].index(False) + 1
    else:
        return -1


print(find_hole(arr))
print(find_hole_2(arr))