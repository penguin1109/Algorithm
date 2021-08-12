# BOJ 1916. 최소 비용 구하기
# 그래프 알고리즘
# A번째 도시에서 B번째 도시까지 가는데 드는 버스 비용을 최소화 시키려고 함
# 도시의 번호는 1부터 N까지

import sys
from heapq import heappush, heappop
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

N = int(input())
M = int(input())

routes = [[] for _ in range(N+1)]

for _ in range(M):
    a, b, price = map(int, input().split())
    routes[a].append((b, price))

start, end = map(int,input().split())
dp = [sys.maxsize for _ in range(N+1)]

def price(start):
    dp[start] = 0
    curr = []
    heappush(curr, (0, start))
    while curr:
        p, s = heappop(curr) # 비용, 시작 지점
        if dp[s] < p: # 지정된 start부터 지점 s까지 도착하는데 드는 최소 비용 dp[s]
            continue
        else:
            for a, b in routes[s]: # 도착 도시, 비용
                if dp[a] > b + dp[s]: # (start->a의 최소 비용) > (start->s의 비용 + s->a의 비용)
                    dp[a] = b + dp[s] 
                    heappush(curr, (b+dp[s], a))

price(start)
print(dp[end])



        



