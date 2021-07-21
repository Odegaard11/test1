# Bubble Sort

def bubble(list1):
    swap = 0
    loop = 0

    needSort = True
    while needSort:
        swapInLoop = 0
        for i in range(len(list1)-1):
            if list1[i] > list1[i+1]:
                temp = list1[i]
                list1[i] = list1[i+1]
                list1[i+1] = temp
                swapInLoop += 1

        if swapInLoop == 0:
            needSort = False
        else:
            loop += 1
            swap += swapInLoop

    return loop, swap, list1

length = int(input("length of list : "))
list1 = []
for i in range(length):
    print("{}-th number : ".format(i+1), end="")
    list1.append(int(input()))

result = bubble(list1)
print("loop : {}, swap : {}".format(result[0], result[1]))
for i in range(len(result[2])):
    print(result[2][i], end=" ")