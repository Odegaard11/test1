def possibility(n):
    half = int(n/2)

    for i in range(1,half+1):
        if (n+i+1) % (2*i+1) == 0:
            return True

    return False

list1 = [4,7,9,10,12,13,16,17,19,20]
for i in list1:
    print(possibility(i))