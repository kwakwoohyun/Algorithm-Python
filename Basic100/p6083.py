r, g, b = map(int, input().split())
count = 0
for i in range(0, r, 1):
    for j in range(0, g, 1):
        for k in range(0, b, 1):
            # print(i, j, k)
            print('{} {} {}'.format(i, j, k))
            count = count + 1
print(count)
