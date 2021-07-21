# 임의의 정수 A, B에 대해 A와 B의 최대공약수를 D라고 할 때 AX + BY = D 를 만족하는 정수 X와 Y가 존재한다.
# A와 B가 주어졌을 때 위 식을 만족시키는 X와 Y, 그리고 A와 B의 최대공약수 D를 구하라.

import math

def cdivide(alpha, beta):
    root = min(min(alpha, beta), int(max(alpha, beta) * 0.5 + 1))
    found = False

    while not found:
        if alpha % root == 0 and beta % root == 0:
            found = True
        else:
            root -= 1

    return root

def euclid(alpha, beta):
    divide = cdivide(alpha, beta)
    a = alpha // divide
    b = beta // divide

    x = 0
    y = 0
    for i in range(1,b):
        if a*i % b == 1:
            x = i
            break
    for i in range(1,a):
        if b*i % a == 1:
            y = i
            break

    if a*x + b*y == a*b+1:
        if abs(x) + abs(y-a) <= abs(x-b) + abs(y):
            y -= a
        else :
            x -= b

    return x, y, divide

print(euclid(4,6))