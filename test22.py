# 초완전수

import math

def realDivSum(n):
    divSum = 1
    root = int(math.sqrt(n))
    for i in range(2, root):
        if n % i == 0:
            divSum += i
            divSum += int(n / i)
    if root == n / root:
        divSum += root
    else:
        if n % root == 0:
            divSum += root
            divSum += int(n / root)

    return divSum

def hyperfect(n):
    isHyperfect = False
    k = 1
    divSum = realDivSum(n)

    if divSum == 1:
        return isHyperfect, 0

    while n >= 1 + k * (divSum - 1):
        if n == 1 + k * (divSum - 1):
            isHyperfect = True
            break
        else:
            k += 1

    return isHyperfect, k

def printer(n):
    for i in range(2, n+1):
        temp = hyperfect(i)
        if temp[0]:
            print(i, temp[1])

printer(1000)

