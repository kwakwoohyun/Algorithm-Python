# 격자판의 세로 h
# 격자판의 가로 w
# 막대의 개수 n
# 각 막대의 길이 l
# 막대를 놓는 방향 d (가로=0, 세로=1)
# 막대를 놓는 막대의 가장 왼쪽 또는 위쪽의 위치 x, y
h, w = map(int, input().split())
n = int(input())
checker_board = [[0] * w for _ in range(h)]
for i in range(n):
    l, d, x, y = map(int, input().split())
    # 가로
    if d == 0:
        for j in range(l):
            checker_board[x - 1][y - 1 + j] = 1
    # 세로
    elif d == 1:
        for j in range(l):
            checker_board[x - 1 + j][y - 1] = 1

for i in checker_board:
    print(*i)
