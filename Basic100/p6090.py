a, m, d, n = map(int, input().split())
for i in range(1, n, 1):
    a = a * m + d
print(a)
