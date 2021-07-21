# m개의 계단을 최대 j칸씩 올라갈 때 총 경우의 수

def hypi(height, max):
    if max == 1:
        return 1
    if height == 1 or height == 0:
        return 1

    temp = min(height, max)
    result = 0
    for i in range(temp):
        result += hypi(height-1-i, max)

    return result

print(hypi(8,3))