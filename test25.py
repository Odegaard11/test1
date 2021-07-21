import random
from itertools import combinations

people = int(input("number of people : "))
weight = []
for i in range(people):
    weight.append(int(random.random() * 450) + 1)

weightList = list(combinations(weight, int(people / 2)))

min = 0
half = 0
for i in range(people):
    min += weight[i]
    half += weight[i]/2

for i in range(len(weightList)):
    temp = 0
    for j in range(int(people / 2)):
        temp += weightList[i][j]

    diff = abs(half - temp)

    if min > diff:
        min = diff

print(half - diff, half + diff)