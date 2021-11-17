# 22865- 가장 먼 곳
import sys,math
from heapq import *
input = sys.stdin.readline

N = int(input())
a,b,c = map(int, input().split())
M = int(input())
# lengths = [[math.inf for _  in range(N+1)]for _ in range(N+1)]
maps = [[]for _ in range(N+1)]
for _ in range(M):
    start, end, cost = map(int, input().split())
    heappush(maps[start], (cost, end))
    heappush(maps[end], (cost, start))

def djastra(start):
    dist = [math.inf for _ in range(N+1)]
    dist[start] = 0
    q = [(0, start)]
    while q:
        cost, place = heappop(q)
        if cost > dist[place]:
            continue
        for tup in maps[place]:
            c, p = tup[0], tup[1]
            temp = c + dist[place]
            if (temp < dist[p]):
                dist[p] = temp
                heappush(q, (temp, p))
    return dist

A = djastra(a)
B = djastra(b)
C = djastra(c)

"""
answer_dist = -1
answer_land = -1
for i in range(1, N+1):
    a_,b_,c_ = A[i], B[i], C[i]
    dist = min(a_,b_,c_)
    if dist > answer_dist:
        answer_dist = dist
        answer_land = i
    elif (dist == answer_dist):
        answer_land = min(answer_land, i)
# print(answer_land)
"""

distance = [A,B,C]
ret = list(map(min, zip(*distance)))
print(ret.index(max(ret[1:])))

