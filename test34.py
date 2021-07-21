# 수직선 위에서 정수 x에서 정수 y로 이동하는 과정을 생각해보자.
# 각 단계의 길이는 음이 아니어야 하며 이전 단계의 길이보다 1이 작거나, 같거나, 1이 커야 한다.
# x에서 y로 가는 데 필요한 최소 단계의 수는 얼마인가? 첫번째와 마지막 단계의 길이는 모두 1이어야 한다.

def steps(diff):

    count = 1
    while count**2 <= diff:
        count += 1

    count -= 1
    loss = diff - count**2

    if count < loss:
        return 2*count + 1
    elif 0 < loss:
        return 2*count
    elif 0 == loss:
        return 2*count-1

    return diff

length = int(input("length : "))
entry = []
for i in range(length):
    temp = []
    print("{}-th entry".format(i+1))
    temp1 = int(input("alpha : "))
    temp2 = int(input("beta : "))
    temp.append(temp1)
    temp.append(temp2)
    entry.append(temp)

for i in range(length):
    diff = entry[i][1] - entry[i][0]
    print(steps(diff))