# 손익분기점

a = int(input("alpha : "))
b = int(input("beta : "))
c = int(input("gamma : "))

def compute(a,b,c):
    k = 1
    if c <= b:
        return 1

    while k * c <= a + k * b:
        k += 1

    return k

print(compute(a,b,c))