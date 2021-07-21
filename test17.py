# 프로도 네오 비밀지도
import random

length = 5
def trans(decimal):
    binary = []
    for i in range(length):
        if decimal >= 2**(length-1-i):
            binary.append(1)
            decimal -= 2**(length-1-i)
        else:
            binary.append(0)

    return binary

map1 =[]
map2 = []
final = []

for i in range(length):
    map1.append(int(random.random() * 2**length))
    map2.append(int(random.random() * 2**length))


for i in range(length):
    temp = []
    alpha = trans(map1[i])
    beta = trans(map2[i])
    for j in range(length):
        if alpha[j] == 0 and beta[j] == 0:
            temp.append(0)
        else:
            temp.append(1)
    final.append(temp)

for i in range(length):
    for j in range(length):
        if final[i][j] == 0:
            print(" ", end="")
        else:
            print("#", end="")
    print()
