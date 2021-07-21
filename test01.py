temp = input("number : ").split(' ')
alpha = int(temp[0])
beta = int(temp[1])
beta = min(beta, alpha-beta)

count2 = 0
count5 = 0

for i in range(alpha-beta+1, alpha+1):
    temp = i
    while temp % 5 == 0:
        count5 += 1
        temp = temp / 5
    while temp % 2 == 0:
        count2 += 1
        temp = temp / 2


for i in range(2, beta+1):
    temp = i
    while temp % 2 == 0:
        count2 -= 1
        temp = temp / 2
    while temp % 5 == 0:
        count5 -= 1
        temp = temp / 5

print(min(count2, count5))