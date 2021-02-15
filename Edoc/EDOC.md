#### 1753 - 최단경로
- 방향그래프가 주어지면 주어진 시작점에서 다른 모든 정점으로의 최단 경로를 구하자
- 모든 간선의 가중치는 10 이하의 자연수
```py
import sys
input = sys.stdin.readline
from queue import PriorityQueue

v, e = map(int, input().split()) # (1<=v<20000, 1<=e<=3000000)
k = int(input()) # 시작 정점의 번호

data = [[] for _ in range(v+1)]
MAX = 9999999999999
dist = [MAX]*(v+1)
arr = PriorityQueue() # (현재 정점의 거리, 현재 정점)의 형태로 값을 저장

for _ in range(e):
    u, v, w = map(int, input().split())
    data[u].append((v, w)) # v = 연결된 노드, w = 가중치

dist[k] = 0
arr.put((0, k))

while (arr.empty() == False):
    temp = arr.get()
    if (temp[0] < dist[temp[1]]):
        continue
    for i in data[temp[1]]:
        node, cost = i[0], i[1]
        if (dist[node] <= temp[0] + cost):
            continue
        else:
            dist[node] = temp[0] + cost
            arr.put((dist[node], node))

for i in range(1, len(dist)):
    if dist[i] != MAX:
        print(dist[i])
    else:
        print('INF')
```

#### 11279 - 최대 힙
- 파이썬의 Priority Queue 모듈만 사용한다면 너무 간단하게 풀 수 있는 문제이다.
- 다만 한가지 차이라면 큰 수부터 출력할 수 있도록 해야 하기 때문에 음수를 붙인 값을 Priority Queue에 입력해서 출력해야 한다.

```py
# 11279 - 최대 힙
# 배열에 자연수 x를 넣고 배열에서 가장 큰 값을 출력한 뒤에 그 값을 배열에서 제거한다.
# 처음에 비어있는 배열에서 시작한다.
# 입력에서 0이 주어진 횟수만큼 답을 출력한다.

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

n = int(input()) # (1 <= n <= 100000)

from queue import PriorityQueue
arr = PriorityQueue()
# 파이썬의 PriorityQueue의 경우에는 최소힙만 가능하기 때문에
# 최댓값을 먼저 꺼내기 위해서는 음수를 붙인 수를 힙에 넣어 주는 것이 맞다.
def solution(k):
    global arr
    if (k == 0):
        if (arr.empty() == True):
            print(0)
        else:
            print(arr.get()*-1) 
    elif (k > 0):
        arr.put(k*-1)

for _ in range(n):
    x = int(input())
    solution(x)
```

#### 10159 - 저울
#### 플로이드 와샬 알고리즘
- 모든 최단 경로를 구하는 방법
- 반복문을 돌리는데에 있어서 index값의 경유점을 반복문의 첫 줄로 결정을 먼저 해야 한다는 사실을 간과하는 바람에 좀 해멨음
  동적 계획법 기법을 사용해서 모든 정점에 대한 최단 경로를 구한다.
```py
# 10159 - 저울
# 무게가 다른 N개의 물건과 물건 쌍의 비교 결과가 주어졌을 때 각 물건에 대해서 그 물건과의 비교 결과를 알 수 없는 물건의 개수를 출력하시오
# i번째 줄에는 물건 i와 비교 결과를 알 수 없는 물건의 개수를 출력한다.

import sys
input = sys.stdin.readline

n = int(input()) # 물건의 개수 (5 <= n <= 100)
m = int(input()) # 물건 쌍의 개수 (0 <= m <= 2000)
answer = [[0]*(n+1) for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split()) # 측정된 물건 무게 (a > b)
    answer[a][b] = 1

# 모든 물건에 대해서 한번씩 DFS를 진행해서 어떤 노드까지 연결이 되어 있는지 확인해 준 뒤에
# 각각의 물건에 대해서 무게의 비교가 불가능한 물건의 개수를 출력하게 된다.



# x와 무게의 대소 비교를 할 수 없는 물건의 개수는 곧 x에서 다른 물건으로 가는 길이 없을 때 이다.
# 그런 의미에서 '모든 노드 사이의 거리'를 구해야 하기 때문에 플로이드 와샬 알고리즘을 사용하는 것이 적절한 것으로 보인다.

for i in range(1, n+1):
    for j in range(1, n+1):
        for k in range(1, n+1):
            # j에서 i까지, i에서 k까지 가는 길이 모두 존재한다면
            if answer[j][i] > 0 and answer[i][k] > 0:
                answer[j][k] = 1

for i in range(1, n+1):
    count = 0
    for j in range(1, n+1):
        if (i != j and answer[i][j] == 0 and answer[j][i] == 0):
            count += 1
    print(count)

print(answer)
```

#### 11780 - 플로이드2
```py
import math
import sys

def warshall(n, dp, dpTrace):
    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                if (i == j):
                    continue
                curr = dp[i][k] + dp[k][j]
                if curr < dp[i][j]:
                    dp[i][j] = curr
                    dpTrace[i][j] = k #최단 거리로 갱신함과 동시에 경유점도 갱신한다.

def route(dpTrace, start, end): 
    #시작점과 도착점이 주어지는 상황에서 dpRoute에 저장된 경유점을 이용해 경로를 반환하는 재귀함수
    if (start == end):
        return []
    else:
        curr = dpTrace[start][end]
        if (curr == None):
            return [start, end]
        else:
            return route(dpTrace, start, curr)[:-1] + route(dpTrace, curr, end)

def main():
    INF = math.inf
    input = sys.stdin.readline
    n = int(input())
    m = int(input())
    dp = [[INF]*(n+1) for _ in range(n+1)]
    dpTrace = [[None]*(n+1) for _ in range(n+1)]
    for _ in range(m):
        a,b,c = map(int, input().split())
        dp[a][b] = min(dp[a][b], c)
    
    warshall(n, dp, dpTrace)
    
    for i in range(1, n+1):
        for j in range(1, n+1):
            if dp[i][j] == INF:
                print(0, end = ' ')
            else:
                print(dp[i][j], end = ' ')
        print()
    
    for i in range(1, n+1):
        for j in range(1, n+1):
            if dp[i][j] == INF:
                print(0, end = ' ')
                continue
            else:
                answer = (route(dpTrace, i, j))
                print(len(answer), *answer)

if __name__ == "__main__":
    main()
```
#### 11567 - 타임머신
```py
# 11657 - 타임머신
# n개의 도시가 존재하고 한 도시에서 출발하여 다른 도시에 도착하는 버스가 m개있다.
# 이동하는데 걸리는 시간이 0이면 순간이동을, 0보다 작으면 시간을 되돌아 간다.
# 1번 도시에서 출발해서 나머지로 가는 가장 빠른 시간을 구하시오

import sys, math
input = sys.stdin.readline

def BelmanFord(n, dp, answer):
    for i in range(n-1): # 시작 노드를 제외한 나머지 노드의 개수만큼
        for j in range(1, n+1): # 모든 edge에 대해서 
            for k in range(1, n+1):
                cost = answer[j] + dp[j][k]
                if answer[k] > cost and answer[j] != INF:
                    answer[k] = cost
                else:
                    continue
    negCycle = True
    for i in range(1, n+1):
        for j in range(1, n+1):
            if answer[j] == INF: 
                continue
            else:
                if answer[j] > answer[i] + dp[i][j]:
                    negCycle = False
                    return negCycle
    return negCycle


def main():
    global INF
    INF = math.inf
    n, m = map(int, input().split())

    # 음의 순환 사이클이 존재한다면 -1을 출력해 주어야 한다.
    # 그렇지 않다면 n-1개의 줄에 걸쳐 각 줄에 1번 도시에서 출발 해 2번, 3번, n번으로 가는 빠른 시간을 순서대로 출력한다.
    # 해당 도시로 가는 경로가 없다면 -1을 출력

    dp = [[INF]*(n+1) for _ in range(n+1)]
    answer = [INF]*(n+1)
    answer[1] = 0
    for _ in range(m):
        a, b, c = map(int, input().split()) # 시작도시, 도착도시, 이동 시간
        dp[a][b] = min(dp[a][b], c)
    
    if BelmanFord(n, dp, answer) == False:
        print(-1)
    else:
        for i in range(2, n+1):
            if answer[i] != INF:
                print(answer[i])
            else:
                print(-1)

    
if __name__ == "__main__":
    main()
```
#### 1865 - 웜홀
- 벨만 포드 문제이다
- 결국에는 그냥 웜홀이 타임머신 문제에서의 음의 가중치를 의미하는 것이고, 시간이 줄어들면서 출발 위치로 다시 돌아온다는 것은 
- 곧 음의 사이클이 존재한다는 것이다.
- 이를 확인해 주기 위해서 갱신을 출발 노드 제외 나머지n-1번, 그리고 계속 감소하는지 보기 위해 한번 더 해서 총 n번 해준다.
```py
# 1865 - 웜홀
# n개의 지점, m개의 도로, w개의 웜홀이 존재한다.
# 시간이 줄어들면서 출발 위치로 돌아오는 것이 가능하면 YES, 불가능하면 NO를 출력한다.

import sys, math
input = sys.stdin.readline
INF = math.inf

# 만약에 n번째 반복에서 갱신이 발생하면 음의 사이클이 존재한다는 뜻이고, 
def BelmanFold(n, dp, answer):
    # 또한 어떠한 수로 시작하는지는 중요하지 않기 때문에 굳이 answer[1] = 0으로 바꾸어 줄 필요 또한 없다.
    # 계속 값이 감소하는지 보기 위해서 n-1번이 아닌 n번까지 갱신을 하고 n번째에도 갱신이 된다면 바로 YES를 출력하면 된다.
    for k in range(n):
        for i in range(1, n+1):
            for node, weight in dp[i]:
                # 여기서 헷갈렸었는데, answer[i]의 값이 inf라는 것을 확인할 필요가 없다.
                cost = answer[i] + weight
                if answer[node] > cost:
                    answer[node] = cost
                    if k == n-1:
                        print('YES')
                        return
    print('NO')
    return
    

def main():
    inf = 9999999999999999999999
    TC = int(input()) # 테스트케이스의 개수
    for _ in range(TC):
        n, m, w = map(int, input().split())
        # 지점의 수, 도로의 개수, 웜홀의 개수
        dp = [[] for _ in range(n+1)] 
        answer = [inf for _ in range(n+1)]
        # 웜홀과 도로 모두 벨만 포드 알고리즘 그대로 적용해서 연결리스트를 만들어서 연결된 노드와 가중치를 저장한다.
        for _ in range(m):
            S, E, T = map(int, input().split())
            # S, E는 연결된 지점의 번호, T는 도로를 통해 이동하는데 걸리는 시간
            # S는 시작 지점, E는 도착 지점, T는 걸리는 시간
            # 도로는 양방향
            dp[S].append([E, T])
            dp[E].append([S, T])
        for _ in range(w): 
            S, E, T = map(int, input().split())
            # 웜홀은 방향성 존재
            dp[S].append([E, -T])
        
        BelmanFold(n, dp, answer)

if __name__ == "__main__":
    main()
```    
