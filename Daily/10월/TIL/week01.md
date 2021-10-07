### ICPC 대비 문제 풀이
#### 17528번 - Two Machines
1. 총 n개의 작업을 완수해야 하는데, 여기서 두대의 machine A, B로 각각의 작업을 완수하는데 걸리는 시간이 다르다
2. 모든 작업을 완수하기 위해서 필요한 최소의 완료 시간을 구하시오

#### Sol 01.
- dp배열에 i번째 작업을 A가 수행할 때에 B가 수행하게 되는 최소의 일의 양을 저장해 놓는다.
- 처음 했을 때는 메모리 초과가 나타났었는데 이는 math.inf라는 너무 큰 수를 사용했기 때문으로, 가능한 최대값인 250x250을 초기 dp의 값으로 설정하니 pypy3로는 통과가 되었다.
- 그러나 python3로는 시간 초과 문제때문에 해결을 할수 없었다. (처음에는)
- 
```python
# 17528 - Two Machines
# 모든 작업을 완료하기 위해서 걸리는 시간의 최솟값을 구하여라

import sys
input = sys.stdin.readline
MAX = 250*250
n = int(input())
A, B = [], []
total = 0
for _ in range(n):
    a, b = map(int, input().split(' '))
    A.append(a)
    B.append(b)
    total += a


dp = [[MAX]*(total+1) for _ in range(n)]

dp[0][total] = 0
dp[0][total-A[0]] = B[0]
for i in range(n-1):
    for j in range(total+1):
        if (dp[i][j] != MAX):
            # i+1번째 작업을 B가 수행하지 않을 때
            dp[i+1][j] = dp[i][j]
            # i+1번째 작업을 B가 수행한다면 A는 i+1번째를 수행하지 않음
            dp[i+1][j-A[i+1]] = min(dp[i+1][j-A[i+1]], dp[i][j] + B[i+1])

answer = MAX
for i in range(total):
    answer = min(answer, max(i, dp[n-1][i]))

print(answer)
```

#### 16367 - TV Show Game
1. 총 k개의 불빛이 있는데 각각은 RB 2개의 색상중 하나이다. 
2. 참가자들에게 k개중에서 3개를 선택하여서 무슨 색일지 맞추어 보라고 한다.
3. 모든 사람들이 2개, 또는 전부 맞출 경우 선물을 받아갈 수 있도록 불빛을 조절해 보자.
- 그래프 이론을 적용해서 모든 경우를 전부 탐색해 보았고, 답은 나왔지만 역시나 메모리 초과가 발생하였다.

### SCC Algorithm
- strongly connected component
1. 타잔 알고리즘
- 모든 정점에 대해서 dfs를 수행하여 scc를 찾는 알고리즘으로, 적용이 비교적 쉽다고 할 수 있다.
    1. 인접 정점에 방문하여 자기 자신을 stack에 넣고 재귀적으로 dfs를 수행한다.
    2. 인접 정점에 방문 했으나 아직 처리중일 경우 작은 값으로 부모값을 갱신
    3. 부모 노드의 dfs가 끝난 경우에는 자신의 id값이 stack에서 나올 때 까지 stack에 있는 node를 pop하고 scc배열에 추가
    4. 만들어진 하나의 scc를 전체 scc배열에 추가
2. 코사라주 알고리즘
- 주어진 방향 그래프의 역방향 그래프와 stack을 사용하여 scc를 구한다.
    1. 주어지는 방향 그래프와 그 그래프의 역방향 그래프를 만든다.
    2. 정점을 담을 stack을 만들고 임의의 정점부터 dfs를 수행
    3. dfs가 끝나는 순서대로 stack에 넣고 아직 방문하지 않은 정점에 대해 dfs를 수행
    4. 모든 정점이 stack에 담긴 이후부터는 stack을 pop해서 나오는 정점부터 역방향 그래프에서 dfs수행
    5. 이때 stack이 빌때까지 탐색되는 모든 정점을 scc로 묶는다.

```python
# 방향 그래프인 경우에만 scc를 적용하는 것이 의미가 있다
# dfs는 총 정점의 개수만큼 수행
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
K, N = map(int, input().split())
graph = [[]for _ in range(2*K+1)]

def neg(x):
    if x <= K:
        return x+K
    else:
        return x-K

def dfs(node):
    global idx, dfs_num
    visit[node] = idx # 노드마다 고유한 번호 할당
    parent = idx 
    idx += 1
    stack.append(node) # 스택에 자기자신을 넣어줌

    for n in graph[node]:
        # 방문을 아직 하지 않은 노드
        if not visit[n]:
            parent = min(parent, dfs(n)) # 작은 값으로 부모값이 갱신되도록함
        # 방문은 되었으나 처리가 되지 않은 노드
        elif not check[n]:
            # 처리가 되지 않은 노드는 현재 dfs를 실행중인 노드
            parent = min(parent, visit[n])
    
    # 부모노드가 자기자신인 경우에는 stack에서 자기자신이 나올때까지 꺼냄
    if parent == visit[node]:
        while stack:
            top = stack.pop()
            check[top] = 1
            dfs_arr[top] = dfs_num
            if node == top:
                break
        dfs_num += 1

    return parent




for _ in range(N):
    a, RB1, b, RB2, c, RB3 = list(input().rstrip().split())
    a, b, c = map(int, [a, b, c])
    if RB1 == 'B': a = a + K
    if RB2 == 'B': b = b + K
    if RB3 == 'B': c = c + K
    graph[neg(a)].append(b)
    graph[neg(b)].append(a)
    graph[neg(b)].append(c)
    graph[neg(c)].append(b)
    graph[neg(c)].append(a)
    graph[neg(a)].append(c)

idx = dfs_num = 0
check = [False for _ in range(2*K+1)]
dfs_arr = [0 for _ in range(2*K+1)]
visit = [0 for _ in range(2*K+1)]
stack = []

for i in range(1, 2*K+1):
    if check[i] == False:
        dfs(i)

for i in range(1, K+1):
    if dfs_arr[i] == dfs_arr[i+K]:
        print(-1)
        exit(0)

for i in range(1, K+1):
    if dfs_arr[i] > dfs_arr[i+K]:
        print('B', end = '')
    else:
        print('R', end = '')
```

### 10.07
#### 프로그래머스 - 가장 먼 노드
1. n개의 노드를 가지는 그래프가 존재할 때 1번 노드에서 가장 멀리 떨어진 노드의 개수를 구하고자 함
- 가장 멀리 떨어진 노드란 최단 경로로 이동했을 때 간선의 개수가 가장 많은 노드를 의미
```python
# 프로그래머스 - 가장 먼 노드
import sys
input = sys.stdin.readline
from collections import deque


def dfs(node,arr):
    global answer
    n = len(arr)
    stack = deque()
    check = [False for _ in range(n+1)]
    check[node] = True
    count = 0
    stack.append((node, 0))
    while stack:
        curr_node, curr_count = stack.popleft()
        for n in arr[curr_node]:
            if check[n] == True:continue
            check[n] = True
            answer[n] = curr_count+1
            stack.append((n, curr_count+1))
        

def solution(n, vertex):
    result = 0
    arr = [[] for _ in range(n+1)]
    for v in vertex:
        a,b = v[0], v[1]
        arr[a].append(b)
        arr[b].append(a)
    dfs(1, arr)
    big = max(answer)
    for a in answer:
        if a == big:result +=1
    return result

n, vertex = 6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
answer = [0 for _ in range(n+1)]
print(solution(n, vertex))
```

#### 프로그래머스 - 빛의 경로 사이클
```python
# 프로그래머스 - 빛의 경로 사이클
# 빛이 이동할 수 있는 경로 사이클의 개수와 각 사이클의 길이를 구하시오
grids = [["SL","LR"],["S"],["R","R"]]
from collections import deque

def cycle(x,y,dir,grid,check):
    # 가로 길이, 세로 길이
    n, m = len(grid[0]), len(grid)
    count = 1
    stack = deque()
    stack.append((x, y, dir))
    while stack:
        a,b,d = stack.popleft()
        count += 1
        a = a%n
        b = b%m
        if count >= (n*m)*(n*m):
            answer.append(count)
            return
        if check[b][a][d] != -1:
            continue
        else:
            check[b][a][d] = count
            
            if grid[b][a] == 'S':
                stack.append((b+dy[d], a+dx[d], d))
            elif grid[b][a] == 'R':
                new_dir = change_dir(d, 'R')
                stack.append((b+dy[new_dir], a+dx[new_dir], new_dir))
            elif grid[b][a] == 'L':
                new_dir = change_dir(d, 'L')
                stack.append((b+dy[new_dir], a+dx[new_dir], new_dir))

dx, dy = [1,0,-1,0], [0,1,0,-1]
def change_dir(dir, ch):
    if ch == 'S':
        return dir
    if ch == 'R':
        dir = dir + 1 if dir < 3 else 0
    else:
        dir = dir - 1 if dir > 0 else 3
    return dir
    


def solution(grid):
    global answer
    dx, dy = [1,0,-1,0], [0,1,0,-1]
    n, m = len(grid[0]), len(grid)
    check = [[[0 for _ in range(4)]for _ in range(n)]for _ in range(m)]
    for y in range(m):
        for x in range(n):
            for i in range(4):
                cur_dir, cur_x, cur_y = i, x, y
                if check[cur_y][cur_x][cur_dir] != 0:
                    continue
                step = 1
                while check[cur_y][cur_x][cur_dir] == 0:
                    check[cur_y][cur_x][cur_dir] = 1
                    step += 1
                    cur_x, cur_y = dx[cur_dir] + cur_x, cur_y + dy[cur_dir]
                    cur_x = cur_x % n
                    cur_y = cur_y % m

                    cur_dir = change_dir(cur_dir, grid[cur_y][cur_x])

                    
                answer.append(step-1)

    return answer

for g in grids:
    answer = []
    print(solution(g))
```