#2020.8.11 - 강한 연결 요소(SCC Algorithm)

#2150 - Strongly Connected Component
#Kosaraju's Algorithm
import sys
sys.setrecursionlimit(10**9)
v,e = map(int, sys.stdin.readline().split())
graph, reverse_graph, visited = [[]for _ in range(v)], [[]for _ in range(v)], [False]*v
stack = []
count = 0
visit = [False]*v
scc = [[]for _ in range(v)]
for _ in range(e):
    a,b = map(int, sys.stdin.readline().split())
    graph[a-1].append(b-1)
    reverse_graph[b-1].append(a-1)

#기본으로 주어진 그래프를 dfs를 이용해 stack에 이동 순서대로 넣음
def dfs(x):
    visited[x] = True
    for k in graph[x]:
        if visited[k] == False:
            dfs(k)
    stack.append(x)

#reverse_graph를 이용해서 scc그래프를 이루는 것의 조합을 구한다.
def make_scc(v,c):
    visit[v] = True
    scc[c].append(v)
    for k in reverse_graph[v]:
        if visit[k] == False:
            make_scc(k,c)
        else:
            continue

#stack에 있는 것을 하나씩 뽑아내면서 scc그룹을 만든다.
def answer():   
    global count
    while stack:
        now = stack[-1]
        stack.pop()
        if visit[now] == False:
            count += 1
            make_scc(now, count-1)

for i in range(v):
    if visited[i] == False:
        dfs(i)
        
answer()
print(count)
for k in range(count):
    scc[k].sort()
    scc[k].append(-2)
#각각의 정점들도 오름차순이어야 하므로 -2를 추가한 뒤 sort한다.
scc = sorted(scc, key = lambda x: x)
for p in range(len(scc)):
    if scc[p]:
        for q in scc[p]:
            print(q+1, end = ' ')
        print()




#2252 - 줄 세우기
#위상 정렬 알고리즘을 bfs알고리즘을 이용해서 해결해야 하는 문제이다.
import sys
n,m = map(int, sys.stdin.readline().split())
graph = [[]for _ in range(n)]
num = [0]*n
for _ in range(m):
    a,b = map(int, sys.stdin.readline().split())
    graph[a-1].append(b-1)
    num[b-1] += 1
from collections import deque
stack = deque()
ans = []
visit = [0]*n
for k in range(n):
    if num[k] == 0:
        visit[k] = 1
        stack.append(k)
def bfs(stack):
    while stack:
        now = stack.pop()
        ans.append(now+1)
        for i in graph[now]:
            if visit[i] == 0 and num[i] > 0:
                num[i] -= 1
            if num[i] == 0:
                visit[i] = 1
                stack.append(i)

bfs(stack)
for i in ans:
    print(i, end = ' ')


#1005 - ACM Craft
#위상 정렬 알고리즘과 dp를 모두 이용하여애 했다.
#사이클이 존재하지 않는 방행그래프인 DAG였지만 그래프를 표로 갱신할 때는 양방향 모두 고려해 주어야 했다.
import sys
t = int(sys.stdin.readline())
for _ in range(t):
    n,k = map(int, sys.stdin.readline().split())
    time = list(map(int, sys.stdin.readline().split()))
    graph = [[]for _ in range(n)]
    num = [0]*n
    graph_test = [[]for _ in range(n)]
    for _ in range(k):
        x,y = map(int, sys.stdin.readline().split())
        graph_test[x-1].append(y-1)
        graph[y-1].append(x-1)
        num[y-1] += 1
    dp = [0]*n
    from collections import deque
    stack = deque()
    visit = [0]*n
    for k in range(n):
        if num[k] == 0:
            visit[k] = 1
            dp[k] = time[k]
            stack.append(k)
    def bfs(stack):
        global dp
        while stack:
            now = stack.pop()
            for i in graph_test[now]:
                if num[i] > 0:
                    num[i] -= 1
                if num[i] == 0:
                    stack.append(i)
                    for k in graph[i]:
                        dp[i] = max(dp[i], dp[k]+time[i])

    bfs(stack)
    w = int(sys.stdin.readline())
    print(dp[w-1])

#4196 - 도미노
#먼저 타잔 알고리즘을 이용하여서 scc그래프를 갱신하고 각 scc그래프를 하나의 노드로 보아 계산을 한다.
#그리고 이는 사이클이 없는 DAG그래프임을 이용하여 indegree,즉 연결을 시도하는(?)노드가 0개, 즉 연결 받는 간선의 개수가 0개인 노드만의 개수를 출력한다.
import sys
sys.setrecursionlimit(10**9)
t = int(sys.stdin.readline())
for _ in range(t):
    n,m = map(int, sys.stdin.readline().split())
    graph = [[]for _ in range(n)]
    for _ in range(m):
        a,b = map(int, sys.stdin.readline().split())
        graph[a-1].append(b-1)


    ids,low = [0]*n, [0]*n
    onstack, stack = [False]*n, []
    count,idx = 0,-1

    def dfs(x):
        global count,idx
        stack.append(x)
        ids[x] = low[x] = idx+1
        idx += 1
        onstack[x] = True
        ids[x] = low[x]
        for k in graph[x]:
            if ids[k] == -1:
                dfs(k)
            if onstack[k]:
                low[x] = min(low[x], low[k])
        if ids[x] == low[x]:
            while stack:
                now = stack.pop()
                onstack[now] = False
                low[now] = low[x]
                if now == x:
                    break
            count += 1
    def findscc():
        for i in range(n):
            ids[i] = -1
        for j in range(n):
            if ids[j] == -1:
                dfs(j)
        return low

    low = findscc()
    ind = [0]*n
    for i in range(n):
        for temp in graph[i]:
            if low[temp] != low[i]:
                ind[low[temp]] += 1
    ans = 0
    low = list(set(low))
    for i in range(count):
        if ind[low[i]] == 0:
            ans += 1
    print(ans)


#4013 - ATM
#첫번째 코드는 비록 시간 초과는 발생했지만 나름대로 구현해보려고 노력한 것이다.
#우선 타잔 알고리즘을 이용해서 SCC를 구성하고 다시 그것들 하나하나를 노드 한개로 보고 그래프의 형태로 재구성하였다.
#그렇게 한 뒤에는 dp의 메모이제이션을 이용하여 만약에 특정 scc의 부분에 restaurant가 존재해서 돈 환산이 가능하다면 최댓값을 갱신하도록 하였다.
import sys
sys.setrecursionlimit(10**7)
n,m = map(int, sys.stdin.readline().split())
graph = [[]for _ in range(n)]
for _ in range(m):
    a,b = map(int, sys.stdin.readline().split())
    graph[a-1].append(b-1)
money = [int(sys.stdin.readline()) for _ in range(n)]
s,p = map(int, sys.stdin.readline().split())
restaurant = [int(i)-1 for i in input().split()]

ids,low = [0]*n, [0]*n
onstack, stack = [False]*n, []
count,idx = 0,-1

def dfs(x):
    global count,idx
    stack.append(x)
    ids[x] = low[x] = idx+1
    idx += 1
    onstack[x] = True
    ids[x] = low[x]
    for k in graph[x]:
        if ids[k] == -2:
            dfs(k)
        if onstack[k]:
            low[x] = min(low[x], low[k])
    if ids[x] == low[x]:
        while stack:
            now = stack.pop()
            onstack[now] = False
            low[now] = low[x]
            if now == x:
                break
        count += 1
def findscc():
    for i in range(n):
        ids[i] = -2
    for j in range(n):
        if ids[j] == -2:
            dfs(j)
    return low

findscc()
available = [False]*n
scc = [[]for _ in range(n)]
for i,j in enumerate(low):
    scc[j].append(i)
    if i in restaurant:
        available[j] = True
dp = [0]*n
def new_dfs(v,start):
    global temp
    for k in scc[v]:
        for p in graph[k]:
            if low[p] != low[start]:
                temp.append(low[p])
                new_dfs(p,start)
    return list(set(temp))
new_graph = []
for i in range(n):
    temp = []
    new_graph.append(new_dfs(i,i))
cost = [0]*n
for i in range(n):
    for k in scc[i]:
        cost[i] += money[k]

dp = [0]*n
from collections import deque
def check(start):
    global visit,visited
    file = deque()
    file.append(start)
    while file:
        a = file.popleft()
        visited[a] = 1
        if available[a]:
            visit[a] = max(cost[a], visit[a])
        for k in new_graph[a]:
            if visited[k] == 0 and available[k]:
                if visit[k] < visit[a] + cost[k]:
                    visit[k] = visit[a]+cost[k]
                    file.append(k)
visit = [0]*n
visited = [0]*n
check(low[s-1])
print(max(visit))

#메모리초과및 시간 초과가 자꾸 발생하는 것으로 보아 처음에 SCC를 구현한 알고리즘에 변형을 주어야 할 것 같다.
import sys
sys.setrecursionlimit(10**9)
n,m = map(int, sys.stdin.readline().split())
graph = [[]for _ in range(n)]
for _ in range(m):
    x,y = map(int, sys.stdin.readline().split())
    graph[x-1].append(y-1)
money = [int(sys.stdin.readline()) for _ in range(n)]
s,p = map(int, sys.stdin.readline().split())
restaurant = [int(i)-1 for i in input().split()]

dfsn = [0]*n
sccn = [-1]*n
stack = []
count, sccnt = 0,0

def scc(v):
    global count, sccnt
    count += 1
    dfsn[v] = ret = count
    stack.append(v)
    for u in graph[v]:
        if dfsn[u] == 0:
            ret = min(ret, scc(u))
        elif dfsn[u] == 1:
            ret = min(ret, dfsn[u])
    if ret == dfsn[v]:
        while stack:
            now = stack.pop()
            sccn[now] = sccnt
            if now == v:
                break
        sccnt += 1
    return ret

for k in range(n):
    dfsn[k] or scc(k)

scc = [[]for _ in range(count)]
for i in range(count):
    scc[sccn[i]].append(i)

def new_dfs(v,start):
    global temp
    for k in scc[v]:
        for p in graph[k]:
            if sccn[p] != sccn[start]:
                temp.append(sccn[p])
                new_dfs(p,start)
    return list(set(temp))
new_graph = []
for i in range(n):
    temp = []
    new_graph.append(new_dfs(i,i))


available = [False]*count
cost = [0]*n
for i in range(count):
    for k in scc[i]:
        cost[i] += money[k]
        if k in restaurant:
            available[i] = True
from collections import deque
visit = [0]*n
def check(start):
    global visit,visited
    file = deque()
    file.append(start)
    while file:
        a = file.pop()
        if available[a]:
            visit[a] = max(visit[a], cost[a])
        for k in new_graph[a]:
            visit[k] = max(visit[k],visit[a]+cost[k])
            file.append(k)


check(sccn[s-1])
print(max(visit))
#결국에 바꾸어서 풀었음에도 변화는 없고 계속 메모리 초과라고 나온다. 보니까 python3로 이 문제를 푼 사람이 많지 않은걸보니 확실히 한계가 있는게 아닐까 싶다.
#일단 dp구현보다도 이 문제에서는 타잔 알고리즘을 이해하고 다양한 방법으로 변형하여 구현하는 것에 집중해야 할 것 같다.
#같은 알고리즘이어도 ssc를 '순서'대로 분류할 수 도 있고 제일 작은 노드를 루트 노드로 생각해서 구분하는 경우 등이 있기 때문이다.
#그래서 맞은 사람들과 내 코드를 비교해서 공부를 좀 해봐야 할것 같다.
