# 강화된 블랙잭
# n장의 카드 중 3장을 뽑아 정해진 값보다 작은 수 중 최대로 만들기

from itertools import combinations

index = int(input("number of cards : "))
max = int(input("max number : "))
cards = []
for i in range(index):
    print("{}-th card : ".format(i+1), end="")
    cards.append(int(input()))

options = list(combinations(cards, 3))
answer = max
for i in range(len(options)):
    now = 0
    for j in range(3):
        now += options[i][j]

    diff = max - now
    if 0 <= diff and diff < answer:
        answer = diff

print(max - answer)