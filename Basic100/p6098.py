x = 10
y = 10
checker_board = [list(map(int, input().split())) for _ in range(y)]
start_x = 1
start_y = 1
while True:
    checker_board[start_x][start_y] = 9
    if checker_board[start_x][start_y + 1] == 0 or checker_board[start_x][start_y + 1] == 2:
        start_y = start_y + 1
        if checker_board[start_x][start_y] == 2:
            checker_board[start_x][start_y] = 9
            break
    else:
        if checker_board[start_x + 1][start_y] == 0 or checker_board[start_x + 1][start_y] == 2:
            start_x = start_x + 1
            if checker_board[start_x][start_y] == 2:
                checker_board[start_x][start_y] = 9
                break
        else:
            checker_board[start_x][start_y] = 9
            break

for i in checker_board:
    print(*i)
