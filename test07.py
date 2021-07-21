# 에라토스테네스의 체

import math

def isPrime(num):
    root = int(math.sqrt(num))

    result = True
    for i in range(2, root+1):
        if num % i == 0:
            result = False
            break;

    return result

def primeCounter(num):
    count = 0
    for i in range(1, num+1):
        if isPrime(i):
            count += 1

    return count

print(primeCounter(1000))