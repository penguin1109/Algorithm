#14267 - 내리 칭찬
#처음에 이 문제를 풀 때에는 매번 받는 칭찬의 입력에 따라서 함수를 실행해 주었기 때문에
#O(N*M)의 시간 복잡도를 가졌었는데, 따라서 시간 초과가 발생하였다.
#그러나 그렇게 하지 않고 한꺼번에 진행을 해주니 452ms의 시간으로 통과가 되었다.
import sys
n,m = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
group = [[]for _ in range(n)]
for i,j in enumerate(num):
    if j != -1:
        group[j-1].append(i)

ans = [0]*n
def addscore(i,w):
    global ans
    from collections import deque
    file = deque()
    file.append(i)
    ans[i] += w
    while file:
        node = file.popleft()
        for k in group[node]:
            ans[k] += w
            file.append(k)
    return
task = [0]*n    
for _ in range(m):
    a,b = map(int, sys.stdin.readline().split())
    task[a-1]+=(b)

for i in range(n):
    if task[i] != 0:
        addscore(i, task[i])
for i in ans:
    print(i,end = ' ')

#16437 - 양 구출 작전
#전위 순회, 중위 순회, 후위 순회 등의 다양한 트리 탐색 방법중에서 선택을 하면 되는데,
#이 문제의 경우에는 후위 순회를 사용하는게 맞았고(리프 노드부터 탐색해야 해서)
#재귀적으로 함수를 호출함으로서 리프 노드에 도달했을 때 다시 되돌아 가며(루트 노드로) 양의 개수 갱신
import sys
n = int(sys.stdin.readline())
sys.setrecursionlimit(10**9)
animal = [0]*n
graph = [[]for _ in range(n)]
for k in range(1,n):
    t,a,p = map(str, sys.stdin.readline().split())
    graph[int(p)-1].append(k)
    animal[k] = int(a) if t == 'S' else int(a)*-1


def postorder(node):
    if graph[node]:
        for k in graph[node]:
            animal[node] += postorder(k)
        return max(animal[node], 0)
    else:
        return max(0, animal[node])
postorder(0)
print(animal[0])


#1068 - 트리
#처음에는 availabel리스츠에 넣어서 사용이 불가능한, 즉 제거해야하는 모든 노드를 없애줄 생각을 했었다.
#그리고 그렇게 했더니 시간 초과없이 무사히 통과했는데, 생각해 보니까 모두 삭제 하지 않아도 그냥
#graph에 저장된 모든 노드들에 포함된 '삭제해야하는 시작 노드'를 제거하면 거기로 이동할 일도, 그래프를 수정할 일도 없이 탐색 가능하다.
count = 0
n = int(input())
tree = list(map(int, input().split()))
map = [[]for x in range(52)]

for i in range(n):
    if tree[i] == -1:
        start = i
    else:
        map[tree[i]].append(i)
go = int(input())

def find(x):
    global count
    if len(map[x]) == 0:
        count += 1
    else:
        for i in map[x]:
            find(i)

for i in range(n):
    if go in map[i]:
        map[i].remove(go)
if start != go:
    find(start)
print(count)


#4803 - 트리
#트리의 성질을 이용하는 문제로,
#1. 임력값으로 트리를 만들고 dfs를 이용해서 간선, 개수를 구한다.
#2, 간선//2 == 노드-1이면 트리개수 += 1
import sys
def dfs(v):
    global node, string
    for k in graph[v]:
        string += 1
        if visit[k] == 0:
            node += 1
            visit[k] = 1
            dfs(k)
case = 0
while True:
    case += 1
    n,m = map(int,sys.stdin.readline().split())
    if n == 0 and m == 0:break
    graph = [[]for _ in range(n)]
    for _ in range(m):
        a,b = map(int, sys.stdin.readline().split())
        graph[a-1].append(b-1)
        graph[b-1].append(a-1)
    visit = [0]*n
    ans = 0
    for i in range(n):
        if visit[i] == 0:
            visit[i] = 1
            node, string = 1,0
            dfs(i)
            if node-1 == string//2:
                ans += 1
    if ans == 0:
        print('Case %s: No trees.'%(str(case)))
    elif ans == 1:
        print('Case %s: There is one tree.'%(str(case)))
    else:
        print('Case %s: A forest of %s trees.'%(str(case),str(ans)))
