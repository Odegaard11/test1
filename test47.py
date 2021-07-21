# 소인수분해

import math

def isPrime(p):
    root = int(math.sqrt(p))

    for i in range(2, root+1):
        if p % i == 0:
            return False

    return True


def divider(n):
    temp = n
    half = int(n/2)
    for i in range(2, half+1):
        if isPrime(i):
            while temp % i == 0:
                print(i)
                temp = temp / i

divider(18991325453139)