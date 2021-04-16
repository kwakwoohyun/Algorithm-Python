import sys

N = int(sys.stdin.readline())
origin_N = N
sum = 0
new = N
while True:
    if int(new) > 9:
        for i in range(2):
            a = new % 10
            sum = sum + a
            new = new // 10
    else:
        sum = N
    print(new)
    print(sum)
    new = str(new % 10) + str(sum)
    if origin_N == int(new):
        print(origin_N)
        break
# list_n = list(str(N))
# if len(list_n) == 1:
#     list_n.append('0')
#     list_n.reverse()
# while True:
#     sum = 0
#     for i in list_n:
#         sum = sum + int(i)
#         list_n = [str(list_n[1]), str(sum)]
#         print(list_n)
#
