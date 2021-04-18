import sys

N = int(sys.stdin.readline())
number_list = list(map(int, sys.stdin.readline().split()))
print()
print(min(number_list), max(number_list))