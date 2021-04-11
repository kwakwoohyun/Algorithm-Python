x = 19
y = 19
# Python Comprehension
checker_board = [list(map(int, input().split())) for _ in range(x)]
count = int(input())
for i in range(count):
    a, b = map(int, input().split())
    for i in range(y):
        if checker_board[a-1][i] == 1:
            checker_board[a-1][i] = 0
        elif checker_board[a-1][i] == 0:
            checker_board[a-1][i] = 1
    for i in range(x):
        if checker_board[i][b-1] == 1:
            checker_board[i][b-1] = 0
        elif checker_board[i][b-1] == 0:
            checker_board[i][b-1] = 1

for i in checker_board:
    print(*i)
