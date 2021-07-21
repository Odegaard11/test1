# 몬테카를로 시뮬레이션으로 원주율 구하기

import random

count = 0
for i in range(100000001):
    x = random.random()
    y = random.random()
    result = x**2 + y**2
    if result <= 1:
        count += 1

print(count/100000000*4)