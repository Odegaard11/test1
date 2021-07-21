# 1 부터 9까지의 연속된 수를 + 나 - 를 사용하여 합계가 100이 되는 전체 수를 구하시오.
# ex) 1 + 2 + 3 - 4 + 5 + 6 + 78 + 9 = 100

list1 = []
for i in range(8):
    list1.append(i+1)
    list1.append("")
list1.append(9)

for v1 in range(3):
    for v2 in range(3):
        if v1 + v2 == 0:
            continue
        for v3 in range(3):
            if v2 + v3 == 0:
                continue
            for v4 in range(3):
                if v3 + v4 == 0:
                    continue
                for v5 in range(3):
                    if v4 + v5 == 0:
                        continue
                    for v6 in range(3):
                        if v5 + v6 == 0:
                            continue
                        for v7 in range(3):
                            if v6 + v7 == 0:
                                continue
                            for v8 in range(3):
                                if v7 + v8 == 0:
                                    continue
                                list1[1] = v1
                                list1[3] = v2
                                list1[5] = v3
                                list1[7] = v4
                                list1[9] = v5
                                list1[11] = v6
                                list1[13] = v7
                                list1[15] = v8

                                for i in range(1,16,2):
                                    if list1[i] == 1:
                                        list1[i] = "+"
                                    elif list1[i] == 2:
                                        list1[i] = "-"
                                    else:
                                        list1[i] = ""

                                temp = list1.copy()

                                for i in range(1,16,2):
                                    if temp[i] == "":
                                        temp[i-1] = 10*temp[i-1] + temp[i+1]
                                        temp[i] = "+"
                                        temp[i+1] = 0

                                sum = temp[0]
                                for i in range(1,16,2):
                                    if temp[i] == "+":
                                        sum += temp[i+1]
                                    else:
                                        sum -= temp[i+1]

                                if sum == 100:
                                    for i in range(17):
                                        print(list1[i], end="")
                                    print(" = 100")