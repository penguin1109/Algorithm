#### 1. BOJ 17968: Fire on Field
- 사실 문제 이해가 영어라서 조금 헷갈렸는데, 결국에는 n번째까지의 수를 나열하되, 첫 두수는 각각 1일때에 1 <= k < n//2 인 k에 대해서 dp[i], dp[i-k], dp[i-2*k]가 등차수열을 이루지 않도록 해야 한다.
- 복잡할줄 알았는데 dp라는 배열에 넣어서 l을 2부터 n까지 순서대로 값을 키워 나가면서 가능할 수를 모든 k에 대해서 반복문으로 계산하여서 최종적으로 dp[n]을 출력하면 된다.
```py3
import sys
n = int(sys.stdin.readline())
#dp라는 배열에서 dp[i]에 저장된 값은 i번째 수가 그 이전까지 등차수열을 만족하는 수가 나오지 않도록 하기 위해 할당되어야 하는 수이다.
dp = [0]*1001
dp[0], dp[1] = 1,1

l = 2

while l <= n:
    data = [1]*1001

    k = 1
    #k의 값에 따라 가능한 값을 확인해 본다.
    while l-2 * k >= 0:
        #만약에 등차수열을 이룰 것 같으면 0으로 배열의 값을 바꾸어 준다.
        #이미 더 작은 값을 채워 주었으니 등차수열의 성질을 이용해 확인해 본다.
        data[dp[l-k]*2-dp[l-2*k]] = 0
        k += 1

    for i in range(1, 1002):
        #가능한 자리가 생기면 그 자리에 l값을 넣어 준다.
        if data[i] == 1:
            dp[l] = i
            break
        else:
            continue

    l += 1
    #l이 n이 될때까지 반복해 준다.
print(dp[n])
```


#### BOJ 17969 : Gene Tree
- 트리와 동적 계획법을 이용하는 문제였는데, 처음에는 문제 이해조차 어려웠다.
- n개의 노드가 있음을 첫 입력값에서 알려주고, 이어지는 n-1줄의 입력값은 각각 노드 번호 두개와 그 연결의 경로의 길이를 의미하는 3개의 값을 알려준다.
- 이를 연결해 보면 rootless-tree의 형태가 완성이 되는데, 이를 이용해서 가능한 **모든 경로**의 제곱 합을 구해야 한다.
  - 단, 주의해야 할 점은 교차로, 즉 아무것도 없지만 노드들을 연결해주기 위한 노드에서 시작하거나 도착하는 경로는 제외해야 한다는 것이다.
```py3
import sys
sys.setrecursionlimit(10**8)
n = int(sys.stdin.readline())
maxx = 0
board = [[maxx]*n for _ in range(n)]

for _ in range(n-1):
    a,b,c = map(int, sys.stdin.readline().split())
    a -= 1
    b -= 1
    board[a][b] = c
    board[b][a] = c
root = []

for i in range(n):
    count = 0
    for j in range(n):
        if board[i][j] != maxx:count += 1
    if count == 3:root.append(i)

def find_route(start, now):
    for i in range(n):
        if board[now][i] != maxx:
            board[start][i] = board[start][now] + board[now][i]

for i in range(n):
    for j in range(i+1, n):
        if board[i][j] != maxx:
            find_route(i,j)
answer = 0
for i in range(n):
    for j in range(i+1, n):
        if i not in root and j not in root:
            answer += board[i][j]**2


print(answer)
```
- 위와 같은 방법으로 풀어 보았는데 역시나 메모리 초과가 발생하였다.
- 예제에 있는 3개의 경우는 통과 하는데도 불구하고 계속 체점을 시ㅣ면 메모리 초과가 발생하였는데, 재귀를 최소화 했기 떄문에 sys.setrecursionlimit(10**8)은 도움이 되지 않을 것이라고 생각한다.
