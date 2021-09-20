from collections import deque
import math
answer = math.inf
def solution(maps):
    global answer
    check = [[False]*5 for _ in range(5)]
    lengths = [[1]*5 for _ in range(5)]
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    q = deque()
    x, y, length = 0, 0, 0
    check[x][y] = True
    maps[x][y] = 0
    q.append((x, y, length))
    while q:
        a, b, l = q.popleft()
        if a == 4 and b == 4:
            break
        for i in range(4):
            aa, bb = a + dx[i], b + dy[i]
            if (0<=aa<5 and 0<=bb<5 and maps[aa][bb] == 1):
                lengths[aa][bb] = lengths[a][b]+1
                q.append((aa, bb, l+1))
    if lengths[4][4] == 0:
        answer = -1
    else:
        answer = lengths[4][4]
    return answer


maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
print(solution(maps))