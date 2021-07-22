# 돌 게임은 두 명이서 즐기는 재밌는 게임이다.
# 탁자 위에 돌 N개가 있다. 상근이와 창영이는 턴을 번갈아가면서 돌을 가져가며, 돌은 4^x개 만큼 가져갈 수 있다.
# 즉, 가능한 개수는 1, 4, 16, 64, ...개 이다. 4^x개만큼 돌을 가져갈 수 있는 방법이 없는 사람이 게임을 지게 된다.
# 두 사람이 완벽하게 게임을 했을 때, 이기는 사람을 구하는 프로그램을 작성하시오. 게임은 상근이가 먼저 시작한다.

def exp4(n):
    exp = 0
    while 4**exp < n:
        exp += 1
    if 4**exp == n:
        return True
    return False

def stone(n):
    if n == 1:
        return True
    elif n == 2:
        return False
    elif n >= 3:
        if exp4(n):
            return True
        else:
            exp = 0
            while 4**exp < n:
                if not stone(n-4**exp):
                    return True
                exp += 1
            return False

print(stone(7))