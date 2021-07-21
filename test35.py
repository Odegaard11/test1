# 상자 겉넓이
# n*n 눈금에 1*1 상자를 쌓는다. 밑면을 포함한 겉넓이를 구하라

n = int(input("size : "))
boxing = []
for i in range(n):
    temp = []
    for j in range(n):
        print("{}*{} : ".format(i+1, j+1))
        element = int(input("height : "))
        temp.append(element)
    boxing.append(temp)

border = 2 * n**2
for i in range(n):
    max1 = 0
    max2 = 0
    for j in range(n):
        if boxing[i][j] > max1:
            max1 = boxing[i][j]
        if boxing[j][i] > max2:
            max2 = boxing[j][i]
    border += 2*max1 + 2*max2

print(border)