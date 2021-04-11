count = int(input())
number_list = []
for i in range(0, count, 1):
    number_list.append(0)
number_list = list(map(int, input().split()))
number_list.reverse()
for i in number_list:
    print(i, end=' ')
