field = [['X', '-', 'X'], ['O', 'X', 'O'], ['X', 'O', 'O']]
for i in range(3):
    print(field[i])
xWon = False
oWon = False
hasEmptyCells = any('-' in row for row in field)

diagonalSum = 0
backDiagonalSum = 0
for i in range(3):
    rowSum = ord(field[i][0]) + ord(field[i][1]) + ord(field[i][2])
    columnSum = ord(field[0][i]) + ord(field[1][i]) + ord(field[2][i])
    diagonalSum += ord(field[i][i])
    backDiagonalSum += ord(field[i][2 - i])
    if rowSum == 264 or columnSum == 264:
        xWon = True
        break
    if rowSum == 237 or columnSum == 237:
        oWon = True
        break

if diagonalSum == 264 or backDiagonalSum == 264:
    xWon = True
if backDiagonalSum == 237 or diagonalSum == 237:
    oWon = True

if not xWon and not oWon and not hasEmptyCells:
    print("Draw")
elif xWon:
    print("X wins")
elif oWon:
    print("O wins")
else:
    print("Continues")


# Сложность O(1)