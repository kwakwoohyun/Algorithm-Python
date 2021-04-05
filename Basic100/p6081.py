num = int(input(), 16)
for i in range(1, 16):
    print(format(num, 'X') + '*' + format(i, 'X') + '=' + format(num * i, 'X'))