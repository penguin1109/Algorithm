import sys,math
from heapq import *
input = sys.stdin.readline

# 입력 받음
n = int(input())
m = int(input())
bus = [[]for _ in range(n+1)] # 서로 다른 두 도시 사이의 거리의 가중치를 저장하는 배열
dist = [math.inf for _ in range(n+1)] # 주어지는 시작점에서 다른 도시까지의 최단 거리
for _ in range(m):
    start, end, cost = map(int, input().split())
    heappush(bus[start], (cost,end))


order = [i for i in range(n+1)]

S, D = map(int, input().split())
dist[S] = 0
order[S] = 0
q = [(0, S)] # (cost, place)
while q:
    cost, place = heappop(q) 
    if dist[place] < cost:
        continue
    for c, p in bus[place]:
        temp = c + dist[place]
        if temp < dist[p]:
            dist[p] = temp
            heappush(q, (dist[p], p))
            order[p] = place

answer = [D]
print(dist[D])

while (D!=S):
    answer.append(order[D])
    D = order[D]
print(len(answer))
print(' '.join(map(str, answer[::-1])))




