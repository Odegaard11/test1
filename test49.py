# 이후 K개의 줄에 정수가 1개씩 주어진다. 정수는 0에서 1,000,000 사이의 값을 가지며,
# 정수가 "0" 일 경우에는 가장 최근에 쓴 수를 지우고, 아닐 경우 해당 수를 쓴다.
# 정수가 "0"일 경우에 지울 수 있는 수가 있음을 보장할 수 있다.

length = int(input('length : '))
moneyList = []
for i in range(length):
    print('{}th money : '.format(i+1), end="")
    temp = int(input(""))
    moneyList.append(temp)

def calculate(moneyList):
    sum = 0

    while len(moneyList) != 1:
        if moneyList[len(moneyList)-1] == 0:
            moneyList.pop()
            moneyList.pop()
        else:
            sum += moneyList.pop()

    if len(moneyList) != 0:
        sum += moneyList.pop()

    return sum

print(calculate(moneyList))
