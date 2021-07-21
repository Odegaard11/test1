# 자연수 = 제곱수 + 제곱수 + 제곱수 + 제곱수
import math

n = int(input('number : '))
root = int(math.sqrt(n))

result = []

for i in range(1,root+1):
    for j in range(i+1):
        for k in range(j+1):
            for l in  range(k+1):
                if n == i**2 + j**2 + k**2 + l**2:
                    temp = []
                    temp.append(i)
                    if j != 0:
                        temp.append(j)
                        if k != 0:
                            temp.append(l)
                            if l != 0:
                                temp.append(k)
                    result.append(temp)

answer = result[0]
for i in range(len(result)):
    if len(result[i]) < len(answer):
        answer = result[i]

print(answer)