# 1 ~ 10000 8의 개수

count = 0

for i in range(10000):
    if i % 10 == 8:
        count += 1
    if (i % 100) // 10 == 8:
        count += 1
    if (i % 1000) // 100 == 8:
        count += 1
    if i // 1000 == 8:
        count += 1

print(count)