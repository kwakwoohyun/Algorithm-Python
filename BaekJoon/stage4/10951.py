import sys

try:
    while True:
        A, B = map(int, sys.stdin.readline().split())
        print(A + B)
except:
    exit()
