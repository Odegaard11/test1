# combination

def combination(n, k):
    result = 1
    for i in range(n, n-k, -1):
        result *= i
    for i in range(2, k+1):
        result /= i

    return int(result)

print(combination(4,2))