# list의 절반을 날리는 타노스
import random

list1 = [1,2,3,4,5,6,7]

def fingerSanp(alpha):
    deathNote = []
    for i in range(len(alpha)):
        deathNote.append(False)
    victims = int(len(alpha)/2 + random.random())
    count = 0
    while count < victims:
        next = int(len(alpha) * random.random())
        if deathNote[next]:
            continue
        else:
            deathNote[next] = True
            count += 1

    survived = []
    for i in range(len(alpha)):
        if not deathNote[i]:
            survived.append(alpha[i])

    return survived

print(fingerSanp(list1))