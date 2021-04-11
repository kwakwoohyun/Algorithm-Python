# x,y 좌표는 1~19
x = 19
y = 19
checker_board = [[0] * x for _ in range(y)]
count = int(input())
for i in range(1, count + 1):
    a, b = map(int, input().split())
    checker_board[a - 1][b - 1] = 1

for i in checker_board:
    print(*i)