board = [['-' for i in range(8)] for j in range(8)]

def print_board(board):
    for i in range(len(board)):
        for j in range(len(board[i])):
            print(board[i][j], end=' ')
        print()

def is_safe(row, column, board):
    i = row

    while i > 0:
        if board[i][column] == 'Q':
            return False
        i-=1

    i = row
    j = column

    while i > 0 and j > 0:
        if board[i][j] == 'Q':
            return False
        i-=1
        j-=1

    i = row
    j = column

    while i > 0 and j < len(board):
        if board[i][j] == 'Q':
            return False
        i-=1
        j+=1

    return True

def solution(row, board):
    if row == len(board):
        print_board(board)
        print()
        return

    for i in range(len(board)):
        if is_safe(row, i, board):
            board[row][i] = 'Q'
            solution(row + 1, board)
            board[row][i] = '-'


solution(0, board)