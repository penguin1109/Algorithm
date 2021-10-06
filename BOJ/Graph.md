#### BOJ 1260 - DFS와 BFS
```py
# 1260 - DFS와 BFS
import sys
input = sys.stdin.readline

n, m, v = map(int, input().split()) # n = 정점의 개수 (1<=n<=1000) m = 간선의 개수 (1<=m<=10000) v = 탐색을 시작할 정점의 번호
board = [[] for _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    board[a].append(b)
    board[b].append(a)
for i in range(n+1):
    board[i].sort()

from collections import deque
def BFS(check, v):
    left = deque()
    left.append(v)
    check[v] = True
    while left:
        a = left.popleft()
        print(a, end = ' ')
        for node in board[a]:
            if check[node] == False:
                check[node] = True
                left.append(node)
    return
    

def DFS(check, idx):
    check[idx] = True
    print(idx, end = ' ')
    global board
    for node in board[idx]:
        if check[node] == False:
            check[node] = True
            DFS(check, node)

check = [False]*(n+1)
DFS(check, v)
print()
check = [False]*(n+1)
BFS(check, v)
```
#### BOJ 16953 - A->B


```py

# 16953 - A -> B
# 정수 A를 B로 바꾸고자 할 때에 수행 가능한 연산이 2를 곱하거나 뒤에 1을 붙이는 것이 존재
# 최소 연산 수  + 1을 출력하시오

import sys
input = sys.stdin.readline

A, B = map(int, input().split())

from collections import deque
answer = 0
def BFS(num):
    global answer
    # 깊이를 중간에 count에 1을 더해주는 방법으로는 불가능하기 때문에 arr 배열에 같이 저장해 주어야만 한다.
    arr = deque([(str(num), 1)])
    while arr:
        temp, depth = arr.popleft()
        a, b = int(temp)*2, int(str(temp)+'1')
        if (a == B or b == B):
            # 탐색 중간에 B가 제일 먼저 나올 때가 제일 얕은 depth일 것이다.
            answer = depth + 1
            return
        else:
            # 연산을 수행하면 할수록 숫자의 크기는 점점 커질 것이기 때문에 목적지인 B보다 작을 때에만 arr 배열에 넣어준다.
            if (a < B):
                arr.append((a, depth+1))
            if (b < B):
                arr.append((b, depth+1))


BFS(A)
if answer == 0:
    print(-1)
else:
    print(answer)
```    


