# 어떤 자연수에서 자릿수가 점점 커지는 수를 증가수라고 하겠습니다(예: 135689).
# 자연수들 중에서는 그 수와 그 수의 자리의 순서가 반대인 수를 곱했을 때
# (여기서 자리의 순서가 반대가 된다는 것은 숫자의 자리가 앞뒤가 바뀐다는 것입니다, 예: 5319 -> 9135) 증가수가 되는 수들이 있습니다.
# 예를 들어 47과 47의 자리를 바꾼 74를 곱하면 3478이 되는데, 이 수는 증가수입니다.
#
# 세 자리 자연수들 중에 그 수와 그 수의 자리를 바꾼 수의 곱이 증가수가 되는 수는 모두 몇 개입니까?
# (단, 세 자리 자연수의 마지막 자릿수는 0이 아니고, 증가수에는 1335 같은 중간에 자릿수의 크기가 바뀌지 않는 것도 포함됩니다.)

def toStr(n):
    numStr = str(n)
    numList = []
    for i in range(len(numStr)):
        numList.append(int(numStr[i]))

    return numList

def reverse(numList):
    root = int(len(numList)/2)

    for i in range(root):
        temp = numList[i]
        numList[i] = numList[len(numList)-1-i]
        numList[len(numList)-1-i] = temp

    return numList

def toNum(numList):
    num = ""
    for i in range(len(numList)):
        num += str(numList[i])

    return num

def isIncreasing(n):
    numStr1 = toStr(n)
    numStr2 = reverse(numStr1)
    nr = int(toNum(numStr2))

    answer = n * nr
    result = toStr(answer)

    increasing = True

    for i in range(len(result)-1):
        if result[i] > result[i+1]:
            increasing = False

    return increasing, answer

print(isIncreasing(47))