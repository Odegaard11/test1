# 아이스크림 공장에서 생산되는 여러 종류의 아이스크림을 모두 보관 할 수 있도록 하는 최소한의 냉장고 수를 구하라.
# 아이스크림의 보관 온도 범위가 주어짐

length = int(input("number of icecream : "))
hardList = []
for i in range(length):
    temp = []
    print("{}-th icecream".format(i+1))
    min = int(input("min temp : "))
    max = int(input("max temp : "))
    temp.append(min)
    temp.append(max)
    hardList.append(temp)

ref = 1
