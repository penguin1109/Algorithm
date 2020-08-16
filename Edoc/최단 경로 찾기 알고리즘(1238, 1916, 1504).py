#1238 - 파티
import sys
from collections import deque
n,m,x = map(int, sys.stdin.readline().split())
board_1, board_2 = [[]for _ in range(n)], [[]for _ in range(n)]
dp_1, dp_2 = [9999999]*(n+1), [9999999]*(n+1)

def check(start, dp, s):
    file = deque()
    dp[start] = 0
    file.append((0, start))
    while file:
        a,b = file.popleft()
        if dp[b] < a:  #dp리스트 갱신이 무의미
            continue
        for i,j in s[b]:
            if j+a < dp[i]:
                dp[i] = j+a
                file.append((j+a, i))

for _ in range(m):
    a,b,c = map(int, sys.stdin.readline().split())
    board_1[a-1].append((b-1, c))
    board_2[b-1].append((a-1, c))
check(x-1, dp_1, board_1)
check(x-1, dp_2, board_2)
ans = 0
for i in range(n):
    ans = max(ans, dp_1[i]+dp_2[i])
print(ans)


#1916 - 최소 비용 구하
import sys
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
board = [[]for _ in range(n)]
for _ in range(m):
    a,b,c = map(int, sys.stdin.readline().split())
    board[a-1].append((b-1, c))
start, end = map(int, sys.stdin.readline().split())
from heapq import heappop, heappush
file = []
visit = [99999999]*n
heappush(file, (0, start-1))
while file:
    a,b = heappop(file)
    for i,j in board[b]:
        now = a+j
        if visit[i] > now:
            visit[i] = now
            heappush(file,(now,i))
print(visit[end-1])

#기본적인 다익스트라 알고리즘 구현만 가능했다면 풀 수 있는 문제였다. 다만 파이썬의 리스트 구현에 있어서 자꾸만 헷갈리는 부분들이 생기는 것 같다. 일단 []*3을 하면 그냥 []이렇게 되고 [[]for _ in range(3)]을 해야만 [[],[],[]]이렇게 된다.

#1504 - 특정한 최단 경로
#다익스트라 알고리즘을 3번씩 2번 이용해야 하는 문제였기 때문에 다익스트라 알고리즘을 함수로 정의하고 문제를 풀었다. 그렇게 한 이유는 ‘반드시 지나야 하는 정점’이 존재하였고 ‘최단 경로’로 이동해야 한다는 조건이 있었기 때문이다. 시작 노드와 끝 노드는 반드시 0번째와 n-1번쨰여야 했고, 이때 반드시 거쳐야 하는 노드를 각각 first, second 라 한다면
#0 -> first +first -> second + second -> n-1 이나
#0 -> second + second -> first + first -> n-1로 해결하면 된다.
#이 값이 min으로 해도 갱신이 안되면 -1을 출력하도록 했다.
import sys
n,e = map(int, sys.stdin.readline().split())
board = [[]for _ in range(n)]
for _ in range(e):
    a,b,c = map(int, sys.stdin.readline().split())
    board[a-1].append((b-1, c))
    board[b-1].append((a-1, c))
no_1, no_2 = map(int, sys.stdin.readline().split())

from heapq import heappop, heappush
def move(v,x):
    file = []
    visit = [99999999]*n
    heappush(file, (0,v))
    visit[v] = 0
    while file:
        i,j = heappop(file)
        for p,q in board[j]:
            now = q+i
            if visit[p] > now:
                visit[p] = now
                heappush(file, (now, p))
    return visit[x]

ans = 99999999
ans = min(ans, move(0,no_1-1)+move(no_1-1, no_2-1)+move(no_2-1, n-1))
ans = min(ans, move(0, no_2-1)+move(no_2-1, no_1-1)+move(no_1-1, n-1))

if ans == 99999999:
    print(-1)
else:
    print(ans)

