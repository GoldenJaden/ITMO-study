import random
import time


#random_matrix = [[1 if e == 0 or e == 14 else random.choice([0, 1]) for e in range(15)] for e in range(15)]
matrix = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1],
          [1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1], [1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1],
          [1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1], [1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1],
          [1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1], [1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1],
          [1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1],
          [1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1],
          [1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1], [1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
for i in range(15):
    print(matrix[i])

# def pathfinder(grid, location, prev):
#
#     if location[1] == 15:
#         return location
#
#
#
#
#
#     if prev != [[location[0] - 1], [location[1]]] and grid[location[0] - 1][location[1]] == 0 and location[0] - 1 <= len(grid) and location[1] <= len(grid[0]):
#         print(prev, location)
#         pathfinder(grid, (location[0] - 1, location[1]), (location[0], location[1]))
#
#     if prev != [[location[0] + 1], [location[1]]] and grid[location[0] + 1][location[1]] == 0 and location[0] + 1 <= len(grid) and location[1] <= len(grid[0]):
#         pathfinder(grid, (location[0] + 1, location[1]), (location[0], location[1]))
#
#     if prev != [[location[0]], [location[1] - 1]] and grid[location[0]][location[1] - 1] == 0 and location[0] <= len(grid) and location[1] - 1 <= len(grid[0]):
#         pathfinder(grid, (location[0], location[1] - 1), (location[0], location[1]))
#
#     if prev != [[location[0]], [location[1] + 1]] and grid[location[0]][location[1] + 1] == 0 and location[0] <= len(grid) and location[1] + 1 <= len(grid[0]):
#         pathfinder(grid, (location[0], location[1] + 1), (location[0], location[1]))
#     return 0
def pathfinder(grid, location, been, steps):
    #time.sleep(1)

    if (location in been and grid[location[0]][location[1]] < been[been.index(location)]):
        print(location, 'j')

    if location not in been or (location in been and grid[location[0]][location[1]] < been[been.index(location)]):
        steps += 1
        been.append(location)

    grid[location[0]][location[1]] = steps
    #print('\n'.join(['\t'.join([str(cell) for cell in row]) for row in grid]))
    #print()

    if location[1] == 14:
        print(been[-1])
        return

    if grid[location[0] - 1][location[1]] == 0 and location[0] - 1 <= len(grid) and location[1] <= len(grid[0]) and (location[0] - 1, location[1]) not in been:
        pathfinder(grid, (location[0] - 1, location[1]), been, steps)

    if grid[location[0] + 1][location[1]] == 0 and location[0] + 1 <= len(grid) and location[1] <= len(grid[0]) and (location[0] + 1, location[1]) not in been:
        pathfinder(grid, (location[0] + 1, location[1]), been, steps)

    if grid[location[0]][location[1] - 1] == 0 and location[0] <= len(grid) and location[1] - 1 <= len(grid[0]) and (location[0], location[1] - 1) not in been:
        pathfinder(grid, (location[0], location[1] - 1), been, steps)

    if grid[location[0]][location[1] + 1] == 0 and location[0] <= len(grid) and location[1] + 1 <= len(grid[0]) and (location[0], location[1] + 1) not in been:
        pathfinder(grid, (location[0], location[1] + 1), been, steps)

    return 0

pathfinder(matrix, [11, 0], [], 1)
