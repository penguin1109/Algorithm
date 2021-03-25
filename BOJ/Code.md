#### Leet Code - 1304. Find N Unique Integers Sum up to Zero(Easy)
- 중복되지 않는 n개의 실수를 이용해서 합이 0이되도록 하는 프로그램을 짜는 것이 목표이다.
- 해당 프로그램을 짜기 위해서 n이 홀수라면 0을 추가하고 n개가 채워질 때까지 a + (-a) = 0임을 이용해서 1부터 n//2까지의 수를 음수를 붙인 수 와 붙이지 않은 수를 array에 넣어 return해주면 된다.
```py
class Solution():
    def sumZero(self, n):
        answer = []
        if n%2 != 0:
            answer.append(0)
        for i in range(1, n//2+1):
            answer.append(i)
            answer.append(i*-1)
        return answer
```
#### BOJ - 15681. 트리와 쿼리
- 재귀함수와 그래프를 이용해서 answer[root] = max(answer[root] + solution(data, k, answer, check), answer[root])로 갱신을 하고, 해당 노드를 root로 갖고 있는 서브 트리에 속한 노드의 개수를 answer리스트에 입력해 넣는다.
- 처음으로 제대로 재귀함수를 혼자 힘으로 이해해서 푼 것이라서 뿌듯하다.

```py
# 15681 - 트리와 쿼리 
# 간선에 가중치와 방향성이 없는 임의의 트리가 주어질 때에 
# 정점 U를 root로 갖는 subtee에 속한 정점의 수를 구하시오

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)
from collections import deque

# 정답을 출력하는 함수 solution을 만들어 주어야 한다
# dp를 이용한 트리 문제이다.
def solution(data, root, answer, check):
    if data[root]:
        for k in data[root]:
            if check[k] == False:
                check[k] = True
                answer[root] = max(answer[root], answer[root] + solution(data, k, answer, check))
    return answer[root]


def main():
    n, r, q = map(int, input().split()) # 트리의 정점의 수, 루트의 번호, 쿼리의 수
    data = [[]for _ in range(n+1)]
    for _ in range(n-1):
        u, v = map(int, input().split()) # 트리에 속한, u와 v를 양끝점으로 갖는 트리에 속하는 간선
        data[u].append(v)
        data[v].append(u)
    answer = [1]*(n+1) # n개의 노드 모두에 대해서 루트일때에 서브 트리에 속한 노드의 모든 개수 저장
    check = [False] * (n+1)
    check[r] = True
    solution(data, r, answer, check)
    for _ in range(q):
        root = int(input())
        # 주어지는 root의 subtree에 속하는 node의 개수를 solution(root)함수를 이용해서 구한다.
        print(answer[root])

if __name__ == "__main__":
    main()
```
#### BOJ - 17182. 우주 탐사선
- 모든 노드에서 다른 모든 노드로의 최단 거리/가중치를 구해주는 알고리즘인 Floyd Warshall과
- 정해준 행성으로부터 모든 노드를 거치기 위한 최단 경로를 구해주기 위해서 DFS를 사용하였다.
- Floyd는 경유점을 먼저 반복문으로 돌려야 함에 유의
- 이렇게 두 함수를 만드는 과정에서, 특히 DFS를 이용하는 과정에서 check리스트를 반드시 갱신해야만 무한 반복을 안할 수 있음을 기억해야 한다.
- 처음에는 시작 노드를 그냥 첫번째 노드로 잡았었기 때문에 (원래는 정해져 있는데) 계속 시간이 inf가 나왔고,
- **전역 변수를 time으로 잡았는데 main()함수에서 global time으로 선언을 해 주어야 다른 함수에서 사용이 가능했었다.**


```py
# 17182 - 우주 탐사선
# 모든 행성을 탐사하는데 걸리는 최소 시간을 계산하여 한다.
# 다시 시작 행성으로 돌아올 필요는 없으며 이미 방문한 행성도 중복해서 갈 수 있다.


        
def main():
    import sys, math
    global time
    time = 9999999999
    input = sys.stdin.readline
    sys.setrecursionlimit(10**8)

    n, k = map(int, input().split()) # 행성의 개수, 발사 행성의 위치
    data = [[0]*(n) for _ in range(n)]
    for i in range(n):
        times = list(map(int, input().split()))
        for j in range(n):
            data[i][j] = times[j]
    Floyd(data, n)
    visit = [False]*(n)
    visit[k] = True
    DFS(visit, 0, n, data, k, 0)
    print(time)

def Floyd(data, n): # 플로이드 와샬을 이용해서 전체 최단 거리를 구해준다. (각 행성에서 행성 까지의)
    for k in range(n): # 경유점
        for i in range(n):
            for j in range(n):
                cost = data[i][k] + data[k][j]
                if data[i][j] > cost:
                    data[i][j] = cost

def DFS(visit, currTime, n, data, currNode, depth): # 행성 사이의 최단 거리로 초기화한 데이터를 이용해서 전체 최단 시간을 구해준다.
    global time
    if depth == n-1:
        time = min(time, currTime)
        return
    else:
        for i in range(n):
            if visit[i] == False:
                visit[i] = True
                DFS(visit, currTime + data[currNode][i], n, data, i, depth + 1)
                visit[i] = False

if __name__ == "__main__":
    main()
```
#### BOJ - 16639. 괄호 추가하기3
- 괄호 안에 괄호를 추가하는 것이 가능하기 때문에 연산자 간의 우선순위가 존재한다는 점과 괄호 내에 여러개의 연산자가 들어갈 수 있다는 점을 무시할 수 있다.
- 그 이유는 괄호를 원하는 순서대로 묶어주면 되기 때문이다.
  1. i번째 수부터 j번째 수까지 연산을 한 결과의 최대, 최소 2차원 배열을 만든다. (크기는 (n//2+1, n//2+1))
  2. 최종 결과의 최댓값을 계산하기 위해서 (최대, 최소), (최소, 최소), (최소, 최대), (최대, 최대)의 조합으로 계산을 하며 값을 갱신한다.
  3. 최종 결과는 최댓값 배열[0][n//2]에 저장이 되어 있을 것이다.
```py
# 16639 - 괄호 추가하기 3
# 길이가 n인 수식이 존재할 때 왼쪽부터 순서대로 계산해야 하며, 괄호 안에 들어있는 식은 먼저 계산해야 한다.
# 수식에 괄호를 추가하여 만들 수 있는 식의 결과의 최댓값을 구하시오
# 추가하는 괄호의 개수의 제한은 없다.

# 동적 계획법을 이용해서 풀면 해결 될 것으로 예상한다.
# 괄호의 개수에 따라 구분

def calculate(a, b, calc): # 앞부분까지의 연산값, 뒷부분의 연산값, 연산 기호가 주어질 경우 계산 함수
    if calc == '+':
        return (a+b)
    elif calc == '-':
        return (a-b)
    else:
        return (a*b)


def main():
    import sys, math
    input = sys.stdin.readline
    global INF; INF = math.inf
    sys.setrecursionlimit(10**8)

    n = int(input()) # 수식의 길이 (1<=n<=19)
    data = list(input().strip()) # 숫자도 문자열의 형태로 입력 받았으니 나중에 연산시에는 int()로 바꾸어 주는것 잊지 말기
    data = list(map(lambda x: int(x) if x in [str(x) for x in range(0, 10)] else str(x), data))

    MAX = 10
    maxArr, minArr = [[-INF]*(MAX) for _ in range(MAX)], [[INF]*(MAX) for _ in range(MAX)]
    for i in range(n//2+1):
        maxArr[i][i] = minArr[i][i] = data[i*2]
    for count in range(1, n//2+1): # 총 관찰하고자 하는 범위의 크기
        for idx in range(n//2+1-count): # 시작값
            j = count
            for i in range(1, count+1):
                opIdx = (idx+count-j)*2+1 # 연산자의 index
                op = data[opIdx] # 연산자
                available = []
                # minArr의 값도 같이 고려하는이유는 연산자가 곱셈인데 음수 * 음수를 계산해야하는 상황일수도 있기 때문
                available.append(calculate(maxArr[idx][idx+count-j], minArr[idx+i][idx+count], op))
                available.append(calculate(maxArr[idx][idx+count-j], maxArr[idx+i][idx+count], op))
                available.append(calculate(minArr[idx][idx+count-j], maxArr[idx+i][idx+count], op))
                available.append(calculate(minArr[idx][idx+count-j], minArr[idx+i][idx+count], op))
                available.sort()
                j -= 1 # 왼쪽 끝점의 범위를 점점 늘림
                maxArr[idx][idx+count] = max(maxArr[idx][idx+count], available[3])
                minArr[idx][idx+count] = min(minArr[idx][idx+count], available[0])
    answer = maxArr[0][n//2]
    print(answer)

if __name__ == "__main__":
    main()
```    

#### BOJ - 19638. 센티와 마법의 뿅망치
- 그냥 heapq모델을 사용해서 내림차순으로 정렬이 가능하도록 음수를 붙여서 값을 연산하면 풀리는 문제였다.
- 즉, 굳이 우선순위 큐를 구현할 필요는 없었던 것이다.
1. 애초부터 H, 즉 센티의 키를 넘는 거인의 키만 고려해 주면 되는 것이므로 넘거나 같은 키만 heapq.heapop()을 이용해 음수로 바꾸어준 뒤 입력
2. 만약에 제일 큰 거인이 1이면 가능
3. 제일 큰 거인의 키를 추출한 뒤에 이를 2로 나눈 값과 H를 비교해 더 크면 다시 넣어주고 아니라면 다시 넣지 않는다.
4. 마지막에 arr리스트가 비어있으면 가능한 것이고 아니면 모든 거인이 H보다 작은 키를 가지는 것은 불가능하다.
```py
def main():
    import sys
    input = sys.stdin.readline
    import heapq
    arr = []

    N, H, T = map(int, input().split()) # 인구수, 센티의 키, 망치 사용 횟수 제한
    # 우선순위 큐인 heapq 모듈을 사용해야 한다.
    for _ in range(N):
        height = int(input())
        if height >= H:
            heapq.heappush(arr, -1*height)
    # 이제 arr은 배열로 구현된 힙이 된다.
    # 오름차순으로 정렬이 되도록 힙을 새롭게 구현해 보자 (max-heap을 만들어 보자는 의미이다.)
    count = 0
    while (arr and count+1 <= T):
        top = arr[0]
        heapq.heappop(arr)
        if (top == -1):
            heapq.heappush(arr, top)
            break
        top = int(top*-1//2)
        if (top >= H):
            heapq.heappush(arr, -1*top)
        count += 1
    
    if not arr:
        print('YES')
        print(count)
    else:
        print('NO')
        print(arr[0]*-1)

if __name__ == "__main__":
    main()
    
```

#### BOJ - 19637. IF문 좀 대신 써줘
- lower_bound를 사용한다.
- lower_bound라는 이분탐색에서 파생된 개념으로 정렬된 리스트에서 해당 target 값보다 크거나 같은 최초의 위치를 탐색함으로서 해결을 할 수 있다.
- 
```py3
#### 19637. IF문 좀 대신 써줘
# 캐릭터의 전투력은 0이상의 정수
# M개의 줄에 걸쳐 캐릭터의 전투력에 맞는 칭호를 입력 순서대로 출력하시오
# 칭호가 여러 개인 경우 가장 먼저 입력된 칭호 하나만 출력

# 전부 일일히 계산한다면 시간초과가 발생할 것이기 떄문에 map에 key값으로 숫자를 넣고 value값으로 문자열을 넣어서 lower_bound를 사용해서 탐색
# 이분탐색으로 자신보다 크거나 같으면서 가장 작은 수를 찾는다.
def lower_bound(data, target, size):
    start = 0
    end = size-1
    while (start < end):
        mid = (start + end)//2
        if (data[mid][1] >= target):
            end = mid
        else:
            start = mid+1
    return end
def main():
    import sys
    input = sys.stdin.readline

    N, M = map(int, input().split())
    data, level = [], []
    for _ in range(N):
        info = list(map(str, input().split()))
        data.append([str(info[0]), int(info[1])])
    for i in range(M):
        num = int(input())
        index = lower_bound(data,num , len(data))
        print(data[index][0])

if __name__ == "__main__":
    main()
```


