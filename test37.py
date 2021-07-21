# 정렬된 k개의 리스트가 있다.
# k개의 리스트 중 적어도 한개의 숫자를 포함하는 구간 간격이 가장 작은 숫자의 범위를 구하시오.

def existance(min, max, numbers):
    for number in numbers:
        if min <= number and number <= max:
            return True

    return False

list1 = [4, 10, 15, 24, 26]
list2 = [0, 9, 12, 20]
list3 = [5, 18, 22, 30]
length = 1
isList1 = False
isList2 = False
isList3 = False
while not(isList1 and isList2 and isList3):
    for i in range(31-length):
        isList1 = False
        isList2 = False
        isList3 = False
        for e1 in list1:
            if i <= e1 and e1 <= i+length:
                isList1 = True
        for e2 in list2:
            if i <= e2 and e2 <= i+length:
                isList2 = True
        for e3 in list3:
            if i <= e3 and e3 <= i+length:
                isList3 = True

        if isList1 and isList2 and isList3:
            print(i, i+length, length)
            break;

    length += 1