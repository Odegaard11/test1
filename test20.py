# smallest multiple
# 1 ~ 20의 최소공배수

import math

def isPrime(number):
    root = int(math.sqrt(number))

    for i in range(2, root+1):
        if number % i == 0:
            return False

    return True

def primeList(num):
    result = []

    for i in range(2, num+1):
        if isPrime(i):
            result.append(i)

    return result

def multiple(num):
    result = []
    prime = primeList(num)

    def divideByPrime(number):
        temp = number
        expList = []

        for i in range(len(prime)):
            expList.append(0)
            while temp % prime[i] == 0:
                temp = temp / prime[i]
                expList[i] += 1

        return expList

    for i in range(len(prime)):
        result.append(0)

    for i in range(2, num+1):
        for j in range(len(prime)):
            if result[j] < divideByPrime(i)[j]:
                result[j] = divideByPrime(i)[j]

    answer = 1
    for i in range(len(prime)):
        answer *= prime[i]**result[i]

    return answer

print(multiple(20))