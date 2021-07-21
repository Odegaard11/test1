# Happy number

def makeNext(n):
    exp = 0
    next = 0
    while n >= 10**exp:
        next += (n%10**(exp+1)//10**exp)**2
        exp += 1

    return next

def happy(n):
    seq = []
    seq.append(makeNext(n))
    isHappy = False
    while not isHappy:
        temp = makeNext(makeNext(seq[len(seq)-1]))
        if temp == 1:
            isHappy = True
        for i in range(len(seq)):
            if temp == seq[i]:
                return isHappy
        seq.append(temp)

    return isHappy

print(happy(4))