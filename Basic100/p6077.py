a = int(input())
evenSum = 0
for i in range(1, a + 1):
    if i % 2 == 0:
        evenSum = evenSum + i
print(evenSum)