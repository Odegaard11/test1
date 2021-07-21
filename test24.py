# 상품을 받을 확률
# 댓글의 위치는 a < n <= b
# n의 약수 갯수가 짝수라면 당첨
import math

a = int(input("a : "))
b = int(input("b : "))

rootA = int(math.sqrt(a))
rootB = int(math.sqrt(b))

prize = rootB - rootA
reply = b - a

possibility = prize / reply

print(possibility)