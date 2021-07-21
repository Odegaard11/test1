def generator(num):
    if num % 2 == 0:
        return num/2
    else:
        return 3*num + 1

def counter(num):
    count = 1
    temp = num
    while temp != 1:
        count += 1
        temp = generator(temp)

    return count

length = input("a and b : ")
interval = length.split(" ")
alpha = int(interval[0])
beta = int(interval[1])

maxlength = 1

for i in range(alpha, beta+1):
    if counter(i) > maxlength:
        maxlength = counter(i)

print(maxlength)