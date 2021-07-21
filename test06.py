# 덧셈 올림 횟수

def difficulty(alpha, beta):
    alphaList = []
    betaList = []
    resultList = []

    alpha, beta = max(alpha, beta), min(alpha, beta)

    while alpha > 0:
        alphaList.append(alpha % 10)
        alpha = alpha // 10
        betaList.append(beta % 10)
        beta = beta // 10

    for i in range(len(alphaList)):
        if i == 0:
            if alphaList[i] + betaList[i] > 9:
                resultList.append(1)
            else:
                resultList.append(0)
        else:
            if alphaList[i] + betaList[i] + resultList[i-1] > 9:
                resultList.append(1)
            else:
                resultList.append(0)

    sum = 0
    for i in range(len(resultList)):
        sum += resultList[i]

    return sum

print(difficulty(9829301371, 23907598))


