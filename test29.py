# 생성자 중 최솟값 구하기
# 245 + 2 + 4 + 5 = 256 => 245는 256의 생성자

def generate(n):
    numbers = []
    exp = 0
    while 10**exp <= n:
        numbers.append(n // 10 ** exp % 10)
        exp += 1

    result = n

    for i in range(len(numbers)):
        result += numbers[i]

    return result

n = int(input("your number : "))

for i in range(n-60, n):
    if generate(i) == n:
        print(i)
        break