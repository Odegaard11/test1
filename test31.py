# 골드바흐의 추측
import math

def isPrime(prime):
    root = int(math.sqrt(prime))

    for i in range(2, root+1):
        if prime % i == 0:
            return False

    return True

def goldbach(n):
    half = int(n/2)
    tupleList = []
    for i in range(2, half+1):
        if isPrime(i):
            if isPrime(n-i):
                tupleList.append([i, n-i])

    return tupleList

print(goldbach(26))