import timeit
import time
def bucketsort(given):
    blocks = [[] for i in range((max(given) - min(given)) // 10 + 1)]
    negative_blocks = [[] for i in range((max(given) - min(given)) // 10)]
    for i in range(len(given)):
        if given[i] >= 0:
            blocks[given[i] // 10].append(given[i])
        else:
            negative_blocks[given[i] // 10].append(given[i])
    blocks = negative_blocks + blocks
    blocks = [sorted(elem) for elem in blocks]
    return [item for sublist in blocks for item in sublist]

ex = [-82, -96, -46, 97, 95, 86, 44, -93, 31, -33, -9, 96, 8, 56, 72, 51, -67, -12, 55,
      26, 29, 67, 80, -90, -11, -2, -43, -73, -73, -7, 47, -91, 45, -94, 88, 65, -67, 99, 95, -2, 17]
print(bucketsort(ex))

print(timeit.timeit(stmt='bucketsort([-82, -96, -46, 97, 95, 86, 44, -93, 31, -33, -9, 96, 8, 56, 72, 51, -67, -12, 55,'
                   '26, 29, 67, 80, -90, -11, -2, -43, -73, -73, -7, 47, -91, 45, -94, 88, 65, -67, 99, 95, -2, 17])',
              setup='from __main__ import bucketsort', timer=time.perf_counter, number=1, globals=globals()))



