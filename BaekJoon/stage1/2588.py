a = int(input())
b = int(input())
b_list = list(map(int, str(b)))
result = []
for i in range(len(b_list), 0, -1):
    result.append(a * b_list[i - 1])
    print(result)
print(a * b)

# for i in reversed(b):
#     result.append(a * i)
#     print(result)
