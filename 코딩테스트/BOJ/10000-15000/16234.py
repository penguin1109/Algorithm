import sys
from heapq import heappop, heappush
from collections import deque
input = sys.stdin.readline

N, L, R = map(int, input().split())

land = []
for _ in range(N):
    land.append(list(map(int, input().split())))
answer = 0

def graph(r, c):
    global is_true
    temp = []
    temp.append((r,c))
    dx, dy = [1, 0,-1,0], [0, 1,0,-1]
    people, city = land[r][c], 1
    visit[r][c] = True
    curr = deque()
    curr.append((r, c))
    while curr:
        a, b = curr.popleft()
        for i in range(4):
            x, y = dx[i] + a, dy[i] + b
            if x < 0 or x >= N or y < 0 or y >= N:
                continue
            if visit[x][y] == True:
                continue
            if L <= abs(land[a][b] - land[x][y]) <= R:
                people += land[x][y]
                city += 1
                visit[x][y] = True
                curr.append((x, y))
                temp.append((x,y))
    m_p = people//city
    if city > 1:
        is_true = True
        for c,d in temp:
            land[c][d] = m_p


while True:
    is_true = False
    visit = [[False]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if visit[i][j] == False:
                graph(i,j)
    if is_true:
        answer += 1
    else:
        break


print(answer)

