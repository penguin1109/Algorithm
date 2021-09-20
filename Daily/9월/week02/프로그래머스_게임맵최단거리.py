# 게임 맵 최단 거리
# 상대팀 진영에 도착하기 위해서 지나가야 하는 칸의 개수의 최솟값

from collections import deque
import math 
answer = math.inf
from collections import deque
import math
answer = math.inf

# 문제를 풀 때에 maps의 가로와 세로를 반영하지 않고 5x5 matrix일 것이라고만 생각해서 문제가 됬었음
def solution(maps):
    global answer
    n, m = len(maps), len(maps[0])
    check = [[False]*m for _ in range(n)]
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    q = deque()
    x, y, length = 0, 0, 1
    check[x][y] = True
    maps[x][y] = 0
    q.append((x, y, length))
    while q:
        a, b, l = q.popleft()
        if a == n-1 and b == m-1:
            answer = l
            break
        for i in range(4):
            aa, bb = a + dx[i], b + dy[i]
            if (0<=aa<n and 0<=bb<m and maps[aa][bb] == 1 and check[aa][bb] == False):
                check[aa][bb] = True
                q.append((aa, bb, l+1))
    if answer == math.inf:
        answer = -1
        
    return answer
maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]
print(solution(maps))