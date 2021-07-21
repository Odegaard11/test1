# 지뢰찾기

def mineFinder(teritory):
    result = []

    for i in range(len(teritory)+2):
        temp = []
        for j in range(len(teritory[i])+2):
            temp.append(0)
        result.append(temp)

    for i in range(1, len(teritory)+1):
        for j in range(1, len(teritory[i])+1):
            if teritory[i][j] == "*":
                result[i][j] = "*"
                if result[i-1][j-1] != "*":
                    result[i-1][j-1] += 1
                if result[i-1][j] != "*":
                    result[i-1][j] += 1
                if result[i-1][j+1] != "*":
                    result[i-1][j+1] += 1
                if result[i][j-1] != "*":
                    result[i][j-1] += 1
                if result[i][j+1] != "*":
                    result[i][j+1] += 1
                if result[i+1][j-1] != "*":
                    result[i+1][j-1] += 1
                if result[i+1][j] != "*":
                    result[i+1][j] += 1
                if result[i+1][j+1] != "*":
                    result[i+1][j+1] += 1

    return result
teritory = []
result = mineFinder(teritory)
for i in range(1,len(result)-1):
    for j in range(1,len(result[i])-1):
        print(result[i][j], end="")
        print()