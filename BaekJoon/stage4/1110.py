import sys

N = temp_n = int(sys.stdin.readline())
count = 0

while True:
    ten = temp_n // 10 # 2 6 8 4
    one = temp_n % 10 # 6 8 4 2
    sum = ten + one # 8 14 12 6
    count = count + 1 # 1 2 3 4
    temp_n = int(str(one) + str(sum % 10))
    if temp_n == N:
        break

print(count)
