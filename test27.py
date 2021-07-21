# a,b 사이의 완전 제곱수
import math


def findSquare(a,b):
    rootA = int(math.sqrt(a))
    rootB = int(math.sqrt(b))
    sum = 0
    min = (rootA + 1) ** 2

    for i in range(rootA + 1, rootB+1):
        sum += i**2
        print(i**2)

    if rootA == math.sqrt(a):
        sum += rootA**2
        min = rootA**2

    return sum, min

print(findSquare(25, 556))