import sys
t = int(sys.stdin.readline())
from collections import deque
def count(board,x,y):
    global ans
    dx,dy = [-1,1,0,0],[0,0,-1,1]
    file = deque()
    file.append((x,y))
    while file:
        a,b = file.popleft()
        board[a][b] = 0
        for k in range(4):
            i,j = a+dx[k], b+dy[k]
            if 0<= i<n and 0<= j<m:
                if board[i][j] == 1:
                    board[i][j] = 0
                    file.append((i,j))
    ans += 1
    
for _ in range(t):
    m,n,k = map(int, sys.stdin.readline().split())
    board = [[0]*m for _ in range(n)]
    for _ in range(k):
        a,b = map(int, sys.stdin.readline().split())
        board[b][a] = 1
    ans = 0
    for x in range(m):
        for y in range(n):
            if board[y][x] == 1:
                count(board, y,x)
    print(ans)

