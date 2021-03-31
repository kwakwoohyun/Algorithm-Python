f1, f2 = input().split()
# 0이 출력되지 않음
print(round(float(f1) / float(f2), 3))
# 0이 출력되게 하는법
print('%.3f' % round(float(f1) / float(f2), 3))
