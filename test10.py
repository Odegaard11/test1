# 감옥에 120명의 죄수가 있다. 간수는 복도를 120번 동안 다음 조건에 지나간다.
#
# 처음에 문은 모두 닫혀 있다.
# N번째 지나갈 때에는 N의 배수인 문들이 열려 있으면 닫고, 닫혀 있으면 연다.
# 마지막에 문이 열려 있으면 그 방의 죄수는 석방이다.
# 과연 몇 명의 죄수가 석방될까?

def divisorCounter(number):
    count = 0
    for i in range(1, number+1):
        if number % i == 0:
            count += 1

    return count

free = 0
for i in range(1, 121):
    if divisorCounter(i) % 2 == 1:
        print(i)
        free += 1

print(free)