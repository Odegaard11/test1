# 6이 연속 3번 이상 들어가는 숫자 중 n 번째 구하기

def include666(n):
    ns = str(n)

    for i in range(len(ns)-2):
        if ns[i:i+3] == '666':
            return True

    return False

def counter(n):
    count = 0
    answer = 666
    while count < n:
        is666 = include666(answer)
        if is666:
            count += 1
        answer += 1

    return answer - 1

print(counter(60000))
