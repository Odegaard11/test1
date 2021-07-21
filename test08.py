# n! 의 마지막 연속된 0의 갯수

def zeroCounter(n):
    count = 0
    exponential = 1
    while 5**exponential < n:
        count += n // 5**exponential
        exponential += 1

    return count

print(zeroCounter(36))