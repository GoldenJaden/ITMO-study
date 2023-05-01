from random import randint as r
def quicksort(given, start, end):
    if start >= end:
        return
    i, j = start, end
    pivot = given[r(i, j)]
    while i <= j:
        while given[i] < pivot:
            i += 1
        while given[j] > pivot:
            j -= 1
        if i <= j:
            given[i], given[j] = given[j], given[i]
            i, j = i + 1, j - 1
    quicksort(given, start, j)
    quicksort(given, i, end)
    return given
