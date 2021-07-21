# 약수를 모두 찾는 수학 문제를 풀다가 지친 X는 컴퓨터의 도움을 받아 문제를 풀어 보기로 하였다.
# 하지만 계산기를 이용하자니 계산기로 하고 싶지만 찾기도 어려우며, 쉽게 찾아낼 수도 없었다.
# 풀이에 지친 그는 결국 약수들이 가지고 있는 특징을 찾아 결국 몇시간에 걸쳐 복잡한 수라도
# 약수를 찾아줄 수 있고 개수도 알려주는 프로그램을 짜게 된다.

import math

def divisor(number):
    root = int(math.sqrt(number))
    divisorList = []
    for i in range(1, root+1):
        if number % i == 0:
            divisorList.append(i)
            if int(number / i) != i:
                divisorList.append(int(number / i))

    return sorted(divisorList)

print(divisor(8197621))
