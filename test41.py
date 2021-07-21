# 허근까지 표시하는 이차방정식의 해
# real part와 imaginary part 모두 정수로 반올림하여 표기
# ax^2 + bx + c = 0 형태. a,b,c 는 real number
import math


def banolim(x):
    tail = x - int(x)
    if tail < 0.5:
        return int(x)
    else:
        return int(x) + 1

def formular(a,b,c):
    root1 = 0
    root2 = 0
    dis = b**2 - 4*a*c

    if dis >= 0:
        root1 = (-b + math.sqrt(dis))/(2*a)
        root2 = (-b - math.sqrt(dis))/(2*a)
        return str(banolim(root1)), str(banolim(root2))
    else:
        real = -b/(2*a)
        imaginary = math.sqrt(abs(dis))/(2*a)

        root1 = str(banolim(real)) + "+" + str(banolim(imaginary)) + "i"
        root2 = str(banolim(real)) + "-" + str(banolim(imaginary)) + "i"

        return root1, root2

print(formular(1, -4, 3))