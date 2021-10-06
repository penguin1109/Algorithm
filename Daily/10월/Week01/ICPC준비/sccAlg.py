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