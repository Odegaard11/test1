# 임의의 수 x를 입력으로 받고, sin x + cos x를 출력하는 프로그램을 만드시오.
# 단, sin x와 cos x를 구하는 함수를 직접 만들어야 합니다.
# sin x = x - x^3 / 3! + x^5 / 5! - x^7 / 7! + ...입니다.
# cos x = 1 - x^2 / 2! + x^4 / 4! - x^6 / 6! + ...입니다.

import math

def formular(x,n):
    return x**n / math.factorial(n)

def sine(x):
    result = 0
    for i in range(1, 1000, 2):
        if i % 4 == 1:
            result += formular(x,i)
        elif i % 4 == 3:
            result -= formular(x,i)

    return result

def cosine(x):
    result = 0
    for i in range(0, 1000, 2):
        if i % 4 == 0:
            result += formular(x, i)
        elif i % 4 == 2:
            result -= formular(x, i)

    return result

print(cosine(2))