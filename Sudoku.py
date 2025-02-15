board = [
    [7,8,0,4,0,0,1,2,0],
    [6,0,0,0,7,5,0,0,9],
    [0,0,0,6,0,1,0,7,8],
    [0,0,7,0,4,0,2,6,0],
    [0,0,1,0,5,0,9,3,0],
    [9,0,4,0,6,0,0,0,5],
    [0,7,0,3,0,0,0,1,2],
    [1,2,0,0,0,7,4,0,0],
    [0,4,9,2,0,6,0,0,7]
]

def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - -")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")

def find_empty():
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (j, i)  # row, col
            
def check(x, y, v):
    for i in range(len(board[0])):
        if board[y][i] == v and x != i:
            return False

    for i in range(len(board)):
        if board[i][x] == v and y != i:
            return False

    x0 = (x // 3) * 3
    y0 = (y // 3) * 3
    for i in range(3):
        for j in range(3):
            if board[y0 + i][x0 + j] == v and (y0 + i, x0 + j) != (y, x):
                return False

    return True

def solve(bo):
    find = find_empty()
    if not find:
        return True
    else:
        x, y = find
    for i in range(1, 10):
        if check(x, y, i):
            bo[y][x] = i
            if solve(bo):
                return True
            bo[y][x] = 0


while True:
    print_board(board)
    answer = input('x, y, value: ')
    if answer == 'exit':
        break
    if answer == 'solve':
        print('SOLVING')
        solve(board)
        print_board(board)
        break
    answer = answer.split(',')
    x = int(answer[0])
    y = int(answer[1])
    value = int(answer[2])
    print(check(x, y, value))
    if check(x, y, value):
        board[y][x] = value
    else:
        print('Invalid move')    