### BOJ 11437: LCA
- 이 문제는 트리 구조를 이용해서 두 노드의 최소 공통 조상을 찾는 문제이다.
- 전체 트리의 루트 노드는 1로 주어지고, 먼저 주어지는 연결된 노드들을 이용해 class구조의 tree가 아니라 list와 array를 이용한 트리 구조를 만들어 놓은 뒤에
- 각 노드의 parent, depth 리스트를 만든다.
- 이후 아래의 논리를 따르면서 loop를 이용하면 구할 수 있다.
  **논리**
  두 정점 u,v에 대해서 u!=v 라면
  1. depth[u] > depth[v]일 때에 u를 parent[u]로 대체
  2. depth[u] == depth[v]가 되는 순간에도 
    - u != v이면 u와 v를 동시에 parent[u]와 parent[v]로 갱신
    - u == v이면 둘중 하나 출력하고 loop 탈출
  
```py3
import sys
sys.setrecursionlimit(10**12)
n = int(input())
linked = [[]for _ in range(n)]
for _ in range(n-1):
    a,b = map(int, input().split())
    a,b = min(a,b), max(a,b)
    linked[a-1].append(b-1)

parent, depth = [[] for _ in range(n)], [[] for _ in range(n)]
#각각의 노드에 대해서 부모 노드에 대한 정보와 현재 순위에 대한 정보를 기록
def find_info(parent, depth, lev, node, bef):
    parent[node].append(bef)
    depth[node].append(lev)
    for k in linked[node]:
        find_info(parent, depth, lev+1, k, node)

find_info(parent, depth, 0, 0, 0)

#만약에 두 노드이 깊이가 다르다면 같아질 떄 까지 더 깊이가 깊은 것을 
#parent리스트에 있는 부모 노드로 갱신해 주고
#깊이가 같아졌을 떄에 두 노드가 다르다면 두 노드를 모두 부모 노드로 갱신해서 lca함수를 다시 처리한다.
def lca(a,b):
    if a != b:
        while (depth[a] != depth[b]):
            if depth[a] > depth[b]:
                a = parent[a][0]
            else:
                b = parent[b][0]
        if depth[a] == depth[b]:
            if a != b:
                lca(parent[a][0], parent[b][0])
            else:
                print(a+1)
    else:
        print(a+1)
#이렇게 두 노드가 공통의 부모 노드를 만날 때 까지 계속 loop를 돌려주면
#최소 공통 조상을 찾을 수 있게 된다.
m = int(input())
for _ in range(m):
    a,b = map(int, input().split())
    lca(a-1,b-1)
```
