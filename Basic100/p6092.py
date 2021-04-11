count = int(input())
number = input().split()
number = list(map(int, number))
result = []
for i in range(0, 23, 1):
    result.append(0)
for i in range(0, count, 1):
    result[number[i]-1] = result[number[i]-1] + 1
for i in result:
    print(i, end=' ')
