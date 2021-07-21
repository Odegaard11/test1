# 기계의 최대 가성비 구하기

def priceCheck(price, level, subprice, sublist):
    count = 0

    for i in range(len(sublist)):
        newlevel = level + sublist[i]
        newprice = price + subprice

        if newlevel / newprice > level / price:
            level = newlevel
            price = newprice
            count += 1
        else:
            break;
    if count <= 0:
        print('shit')
    else :
        print(level / price)
        for i in range(count):
            print(sublist[i], end=" ")

price = int(input("price of machine : "))
level = int(input("level of machine : "))
miniprice = int(input("price of submachines : "))
length = int(input("number of submachines : "))
sublist = []
for i in range(length):
    print("level of {}-th submachine".format(i+1))
    sublist.append(int(input()))

priceCheck(price, level, miniprice, sublist)
