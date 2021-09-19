import sys
input = sys.stdin.readline

def solution(price, money, count):
    answer = 0
    sum = (count+1)*(count)//2
    answer = max(answer, sum*price-money)
    return answer

price, money, count = 3, 20, 4
print(solution(price, money, count))
