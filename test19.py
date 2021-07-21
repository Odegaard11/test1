# h-index / g-index
# h-index : 인용 횟수가 h번 이상인 논문이 h개일 때 가능한 h의 최댓값
# g-index : 인용 횟수가 높은 상위 g개 논문의 인용 횟수 총합이 g²이상일 때 가능한 g의 최댓값

def hindex(papers):
    papers = sorted(papers, reverse=True)
    h = 0
    for i in range(len(papers)):
        if papers[i] >= i+1:
            h += 1
        else:
            break
    return h

def gindex(papers):
    papers = sorted(papers, reverse=True)
    g = 0
    quotated = 0
    for i in range(len(papers)):
        quotated += papers[i]
        if quotated >= (i+1)**2:
            g += 1
        else:
            break
    return g

papers = [0, 15, 4, 0, 7, 10, 0]
print(hindex(papers), gindex(papers))