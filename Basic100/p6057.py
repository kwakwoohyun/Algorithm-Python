a, b = map(bool, map(int, input().split()))
print((not a and not b) or (a and b))
