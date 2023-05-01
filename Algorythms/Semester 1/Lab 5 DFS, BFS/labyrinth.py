import random

#random_matrix = [[1 if e == 0 or e == 14 else random.choice([0, 1]) for e in range(15)] for e in range(15)]
matrix = [[1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1], [1, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 1, 0, 1],
          [1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 0, 1], [1, 0, 0, 1, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 1],
          [1, 0, 1, 1, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1], [1, 1, 1, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 1, 1],
          [1, 0, 1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 1, 0, 1], [1, 1, 0, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1],
          [1, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0], [1, 1, 1, 0, 1, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1],
          [1, 0, 1, 0, 1, 1, 0, 1, 0, 1, 1, 1, 1, 0, 1], [0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1],
          [1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1], [1, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 1],
          [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]]
for i in matrix:
    for line in i:
        print("{:^3}".format(line), end=" ")
    print("")
# for i in range(15):
#     print(matrix[i])
end = ()
start = (11, 0)

def pathfinder(grid, location, been, weight):
    global end
    weight += 1
    if location not in been:
        been.append(location)

    if location[1] == len(grid)-1:
        end = been[-1]
        return

    if grid[location[0] - 1][location[1]] == 0 and location[0] - 1 <= len(grid) and location[1] <= len(grid[0]) and (location[0] - 1, location[1]) not in been:
        matrix[location[0] - 1][location[1]] = str(weight)
        pathfinder(grid, (location[0] - 1, location[1]), been, weight)

    if grid[location[0] + 1][location[1]] == 0 and location[0] + 1 <= len(grid) and location[1] <= len(grid[0]) and (location[0] + 1, location[1]) not in been:
        matrix[location[0] + 1][location[1]] = str(weight)
        pathfinder(grid, (location[0] + 1, location[1]), been, weight)

    if grid[location[0]][location[1] - 1] == 0 and location[0] <= len(grid) and location[1] - 1 <= len(grid[0]) and (location[0], location[1] - 1) not in been:
        matrix[location[0]][location[1] - 1] = str(weight)
        pathfinder(grid, (location[0], location[1] - 1), been, weight)

    if grid[location[0]][location[1] + 1] == 0 and location[0] <= len(grid) and location[1] + 1 <= len(grid[0]) and (location[0], location[1] + 1) not in been:
        matrix[location[0]][location[1] + 1] = str(weight)
        pathfinder(grid, (location[0], location[1] + 1), been, weight)
    return


def printPath(grid, end):
    y = end[0]
    x = end[1]
    weight = int(grid[y][x])
    result = list(range(weight))
    while (weight):
        weight -= 1
        if y >= 0 and grid[y - 1][x] == str(weight):
            y -= 1
            result[weight] = 'down'
        elif y <= (len(grid) - 1) and grid[y + 1][x] == str(weight):
            result[weight] = 'up'
            y += 1
        elif x >= 0 and grid[y][x - 1] == str(weight):
            result[weight] = 'right'
            x -= 1
        elif x <= (len(grid[y]) - 1) and grid[y][x + 1] == str(weight):
            result[weight] = 'left'
            x += 1

    return result

pathfinder(matrix, [11, 0], [start], 0)
matrix[start[0]][start[1]] = str(matrix[start[0]][start[1]])
print(end)
print(printPath(matrix, end))

for i in matrix:
    for line in i:
        print("{:^3}".format(line), end=" ")
    print("")


