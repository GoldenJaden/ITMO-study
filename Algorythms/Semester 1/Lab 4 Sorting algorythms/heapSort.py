import timeit
import time

def moveDown(Given, start, end):
    largest = 2 * start + 1
    while largest <= end:
        r = largest + 1
        if (largest < end) and (Given[largest] < Given[r]): # if right child > largest
            largest = r
        if Given[largest] > Given[start]: # if right child > root
            Given[largest], Given[start] = Given[start], Given[largest]
            start = largest
            largest = 2 * start + 1
        else:
            return

def heapSort( Given ):
  length = len( Given ) - 1 # convert to heap
  leastParent = length // 2
  for i in range ( leastParent, -1, -1 ):
    moveDown( Given, i, length )

print(timeit.timeit(stmt='heapSort([-82, -96, -46, 97, 95, 86, 44, -93, 31, -33, -9, 96, 8, 56, 72, 51, -67, -12, 55,'
                   '26, 29, 67, 80, -90, -11, -2, -43, -73, -73, -7, 47, -91, 45, -94, 88, 65, -67, 99, 95, -2, 17])',
              setup='from __main__ import heapSort', timer=time.perf_counter, number=1, globals=globals()))