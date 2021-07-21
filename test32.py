# (난이도 up.ver: n과m을 입력받고 m개의 양수의 곱이 n이 되는 모든 양수출력!)

def dividing(n, m):
    if m == 2:
        temp1 = []
        for i in range(1,n+1):
            if n % i == 0:
                tuple1 = []
                tuple1.append(i)
                tuple1.append(int(n/i))
                temp1.append(tuple1)

        return temp1

    elif m > 2:
        temp2 = []
        for i in range(1,n+1):
            if n % i == 0:
                sublist = dividing(int(n/i), m-1)
                for j in range(len(sublist)):
                    temp = sublist[j]
                    temp.insert(0,i)
                    temp2.append(temp)

        return temp2

print(dividing(12,4))