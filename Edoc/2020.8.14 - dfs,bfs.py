#1260 – DFS와 BFS
#dfs
def dfs(v):   #깊이 우선
    visited = [0]*n
    stack = []
    stack.append(v)
    visited[v] = 1
    print(v+1, end = ' ')
    while stack:
        now = stack[-1]
        can_go = False
        for k in range(n):
            if board[now][k] == 1:
                if visited[k] == 0:
                    visited[k] = 1
                    can_go = True
                    stack.append(k)
                    print(k+1, end = ' ')
                    break
        if not can_go:
            stack.pop()

#bfs
from collections import deque
def bfs(v):   #너비 우선
    global visited
    file = deque()
    file.append(v)
    visited[v] = 1
    while file:
        now = file.popleft()
        print(now+1, end = ' ')
        for k in range(n):
            if board[now][k] == 1:
                if visited[k] == 0:
                    visited[k] = 1
                    file.append(k)

#1012 - 유기농 배추
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


#1707 – 이분 그래프
#dfs로 해결
import sys
t = int(sys.stdin.readline())
def dfs(v,num):
    res[v] = num
    ans = True
    for k in board[v]:
        if res[k] == -1:
            if not dfs(k, abs(1-res[v])):
                ans = False
        else:
            if res[k] == res[v]:
                return False
    return ans
for _ in range(t):
    v,e = map(int, sys.stdin.readline().split())
    board = [[]for _ in range(v)]
    for _ in range(e):
        x,y = map(int, sys.stdin.readline().split())
        board[x-1].append(y-1)
        board[y-1].append(x-1)
    res = [-1]*v
    ans = 'YES'
    for k in range(v):
        if res[k] == -1:
            if not dfs(k,1):
                ans = 'NO'
                break
    print(ans)

#bfs로 해결
def check(node):
    file = deque()
    res[node] = 0
    file.append(node)
    while file:
        now = file.popleft()
        for k in board[now]:
            if res[k] == -1:
                res[k] = abs(res[now]-1)
                file.append(k)
            else:
                if res[k] == res[now]:
                    return False
    return True

for _ in range(t):
    v,e = map(int, sys.stdin.readline().split())
    board = [[]for _ in range(v)]
    for _ in range(e):
        a,b = map(int, sys.stdin.readline().split())
        board[a-1].append(b-1)
        board[b-1].append(a-1)
    res = [-1]*v
    ans = 'YES'
    for k in range(v):
        if res[k] == -1:
            if not check(k):
                ans = 'NO'
                break
    print(ans)

#11724 – 연결 요소의 개수
#이전에 풀었던 scc알고리즘에서 제일 중요했던 부분이 바로 이렇게 루트 노드를 찾아내는 방법이었다. 그랬기 때문에 좀더 정확하게, 한번에 해결이 가능했던 것이라고 생각한다.
#bfs(v, num)으로 해서 v번 노드의 루트를 너비 우선 탐색으로 num이라는 수로 변경하는 것이고, 이 또한 이전 이분 그래프 문제와 마찬가지로 방문하지 않은 노드가 없을 때까지 시행했다.

import sys
n,m = map(int, sys.stdin.readline().split())
board = [[]for _ in range(n)]
for _ in range(m):
    u,v = map(int, sys.stdin.readline().split())
    board[u-1].append(v-1)
    board[v-1].append(u-1)
res = [int(i) for i in range(n)]
from collections import deque
visited = [0]*n

def check(v,num):
    file = deque()
    file.append(v)
    while file:
        v = file.popleft()
        for k in board[v]:
            if res[k] == k:
                if visited[k] == 0:
                    res[k] = num
                    visited[k] = 1
                    file.append(k)
                else:
                    res[k] = num
                    check(k,num)
            else:
                if res[k] != num:
                    res[k] = num
                    check(k,num)

for k in range(u):
    if visited[k] == 0:
        visited[k] = 1
        check(k,k)      
print(len(set(res)))




#2667 – 단지 번호 붙이기
import sys
n = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().strip())) for _ in range(n)]
from collections import deque
def move(x,y):
    global board,ans
    file = deque()
    count = 1
    board[x][y] = 0
    file.append((x,y))
    dx,dy = [-1,1,0,0],[0,0,-1,1]
    while file:
        i,j = file.popleft()
        for k in range(4):
            a,b = i+dx[k], j+dy[k]
            if 0<=a<n and 0<=b<n:
                if board[a][b] == 1:
                    board[a][b] = 0
                    file.append((a,b))
                    count += 1
    ans.append(count)
ans = []
cnt = 0
for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            move(i,j)
            cnt += 1
print(cnt)
ans.sort()
for i in ans:
    print(i)

#1697 – 숨바꼭질
#중요한 것을 중복 방문을 막기 위해 다시 visit리스트를 매번 갱신해 주어야 한다는 것과 스택에서 해당 값을 pop해내기 전에 visit리스트를 갱신해 주어야 한다는 것이다. 그리고 visit리스트는 k도달 지점까지가 아니라 최대 가능 좌표의 값으로 설정해야 함에 주의하자.
n,k = map(int, input().split())
visit = [0]*100001
from collections import deque
file = deque()
def move(v):
    file.append((v,0))
    visit[v] = 1
    while file:
        a,b = file.popleft()
        if a == k:
            return b
        num = [a-1, a+1, a*2]
        for i in num:
            if 0<= i <= 100000:
                if visit[i] == 0:
                    file.append((i,b+1))
                    visit[i] = 1
print(move(n))

