# 창영이는 선영이가 사탕을 공평하게 나누어주지 않으면 친구들을 때릴정도로 사탕을 좋아한다.
# 따라서, 선영이는 다음 파티에 사용할 사탕을 구매하기 전에 고민을 하기 시작했다.
# 만약 파티에 K명이 참가한다면, 공정하게 나누어주려면 K×X개를 사야 한다. (X는 자연수)
# 선영이는 항상 적어도 한 아이는 사탕을 잃어버린다는 사실을 알고 있다. 그래서 캔디를 하나 더 구매해 총 (K×X+1)개를 구매하려고 한다.
# 사탕은 봉지 단위로 판매한다. 한 봉지에는 사탕이 총 C개 들어있다.
# 문제의 조건을 만족하면서 구매할 수 있는 사탕 봉지의 개수를 구하는 프로그램을 작성하시오.
# 각 테스트 케이스에 대해서 문제의 조건을 만족시키면서 구매할 수 있는 사탕 봉지가 없다면, "IMPOSSIBLE"을 출력한다.
import math

def isPrime(p):
    root = int(math.sqrt(p))

    for i in range(2, root+1):
        if p % i == 0:
            return False

    return True

def pList(n):
    half = int(n/2)
    primes = []

    for i in range(2,half+1):
        if isPrime(i):
            primes.append(i)

    if isPrime(n):
        primes.append(n)

    return primes

def relativePrime(n,m):
    order = min(n,m)
    primes = pList(order)

    for p in primes:
        if n % p == 0:
            if m % p == 0:
                return False

    return True

def isPossible(k,c):
    if not relativePrime(k,c):
        print('Impossible')
    elif relativePrime(k,c):
        trial = 0
        founded = False
        while not founded:
            if (c*trial - 1)/k == int((c*trial - 1)/k):
                print(trial)
                founded = True
            else:
                trial += 1

isPossible(1337, 23)

