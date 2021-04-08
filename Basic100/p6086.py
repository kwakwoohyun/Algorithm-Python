num = int(input())
sum = 0
i = 0
while True:
    sum = sum + i
    i = i + 1
    if sum >= num:
        break
print(sum)
