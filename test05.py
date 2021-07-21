# 10진수를 n진수로 변환

def operater(num, ruler):
    cylinder = []
    divided = num
    isTrue = True
    while isTrue:
        if divided % ruler < 10:
            cylinder.append(divided % ruler)
        else:
            if divided % ruler == 10:
                cylinder.append("a")
            if divided % ruler == 11:
                cylinder.append("b")
            if divided % ruler == 12:
                cylinder.append("c")
            if divided % ruler == 13:
                cylinder.append("d")
            if divided % ruler == 14:
                cylinder.append("e")
            if divided % ruler == 15:
                cylinder.append("f")
        divided = divided // ruler
        if divided == 0:
            isTrue = False

    result = ""
    for i in range(len(cylinder)):
        result = str(cylinder[i]) + result

    return result
num = int(input("your number : "))
ruler = int(input("from 2 to 16 : "))

print(operater(num, ruler) + "(" + str(ruler) + ")")