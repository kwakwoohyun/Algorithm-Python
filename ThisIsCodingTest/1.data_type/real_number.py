# 양의 실수
a = 157.93
print(a)
print(type(a))

# 음의 실수
a = -1837.2
print(a)
print(type(a))

# 소수부가 0일때 0을 생략
a = 5.
print(a)
print(type(a))

# 정수부가 0일때 0을 생략
a = -.7
print(a)
print(type(a))

# 지수 표현 방식
# 1,000,000,000의 지수 표현방식
a = 1e9
print(a)
# 실수형을 정수형으로 변환
print(int(a))

# 752.5
a = 75.25e1
print(a)

# 3.954
a = 3954e-3
print(a)

# round() 함수를 사용해야 하는 이유
a = 0.3 + 0.6
print(a)
if a == 0.9:
    print(True)
else:
    print(False)

a = round(a, 2)
print(a)
if a == 0.9:
    print(True)
else:
    print(False)

# 연산
a = 7
b = 3

# 나누기 -> 값이 항상 실수형(float)이 반환된다.
print(a / b)
# 나머지
print(a % b)
# 몫
print(a // b)
# 거듭제곱
print(a ** b)
# 제곱근
print(a ** 0.5)
