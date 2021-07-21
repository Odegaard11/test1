# 약 2,000년 전에는 전쟁에서 병사들이 적들에 의해 동굴에 갇히게 되는 경우가 종종 있었다고 한다.
#
# 그들은 포로가 되는것을 방지하기 위해 동그랗게 서서 마지막 한 사람이 남을 때 까지 순서대로 돌아가며 세번째에 해당되는 사람을 죽여 나갔다고 한다.
#
# 마지막으로 남게되는 사람은 자살하기로 약속되어 있었지만 보통 적들에게 항복을 하는 경우가 많았다고 한다.
#
# 여러분이 풀어야 할 문제는 총 인원수(N)와 간격(K)이 주어졌을 때 가장 마지막에 살아남는 병사의 위치(the safe position)를 알아내는 것이다.
#
# 예를 들어 병사수가 총 10명이고 돌아가며 세번째에 해당되는 병사를 제거하는 경우는 다음과 같다:

def josephus(alpha, beta):
    survived = []
    count = 0
    dead = 0

    for i in range(1, alpha+1):
        survived.append([i, True])

    while dead < alpha-1:
        print(survived)
        for i in range(alpha):
            if survived[i][1]:
                count += 1
                if count == beta:
                    survived[i][1] = False
                    dead += 1
                    count = 0

    result = 0
    for i in range(alpha):
        if survived[i][1]:
            result = survived[i][0]
            break;

    return result
print(josephus(10, 3))