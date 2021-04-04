num = int(input())
num_sum = 0
for i in range(1, num + 1, 1):
    num_sum = num_sum + i
    if num_sum >= num:
        print(i)
        break
