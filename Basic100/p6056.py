a, b = map(bool, map(int, input().split()))
print((a and not b) or (not a and b))