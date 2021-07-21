# 어떤 수를 소수의 곱으로만 나타내는 것을 소인수분해라 하고, 이 소수들을 그 수의 소인수라고 한다.
#
# 예를 들면 13195의 소인수는 5, 7, 13, 29 이다.
#
# 600851475143의 소인수 중에서 가장 큰 수를 구하시오.

import math

def isPrime(number):
    root = int(math.sqrt(number))

    for i in range(2, root+1):
        if number % i == 0:
            return False

    return True

def divideByPrime(number):
    temp = number
    root = int(math.sqrt(number))
    primeList = []

    for i in range(2, root+1):
        if isPrime(i):
            while temp % i == 0:
                temp = temp / i
                primeList.append(i)

                if temp == 1:
                    return primeList

    return primeList

for i in range(len(divideByPrime(600851475143))):
    print(divideByPrime(600851475143)[i], end=" ")