# Road Reconstruction
# 그래프 이론, 다익스트라

import sys
from collections import deque
input = sys.stdin.readline
import heapq, math

m, n = map(int, input().split())
maps = []
result = -1
def BFS(maps, check, x, y):
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    if x == n-1 and y == m-1:
        return check
    for i in range(4):
        a, b = x + dx[i], y + dy[i]
        if (0<=a<n and 0<=b<m):
            if maps[b][a] != -1:
                check[b][a] = min(check[b][a], maps[b][a] + check[y][x])
                BFS(maps, check, a, b)

def bfs(maps, check):
    global result
    x, y = 0, 0
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    answer = maps[0][0]
    if maps[0][0] != -1:
        maps[0][0] = 3
    q = []
    heapq.heappush(q, (answer,0,0))
    while q:
        curr = heapq.heappop(q)
        cost,x,y = curr[0], curr[1], curr[2]
        if (x == n-1 and y == m-1):
            answer = cost
            check[y][x] = cost
            return check
        for i in range(4):
            a, b = x + dx[i], y + dy[i]
            if (0<=a<n and 0<=b<m):
                if maps[b][a] != -1 and maps[b][a] != 3:
                    heapq.heappush(q, (cost+maps[b][a], a, b))
                    check[b][a] = min(check[b][a], cost + maps[b][a])
                    maps[b][a] = 3
    return check
for _ in range(m):
    maps.append(list(map(int, input().split())))

def solution(maps):
    if maps[0][0] == -1 or maps[m-1][n-1] == -1:
        print(-1)
        return

    check = [[math.inf]*n for _ in range(m)]
    result = bfs(maps, check)
    if result[m-1][n-1] == math.inf:
        print(-1)
        return
    print(result[m-1][n-1])

solution(maps)

