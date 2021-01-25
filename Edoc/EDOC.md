#### 14494 - 다이나믹이 뭐예요?
```py3
# 14494 - 다이나믹이 뭐예요?

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

n, m = map(int, input().split()) # 1<=n, m<=1000
div = 1000000007

# dp[i][j] = dp[i-1][j] + dp[i][j-1]

dp = [[0] * (m+1) for _ in range(n+1)]

dp[0][0] = 1

for i in range(1, n+1):
    for j in range(1, m+1):
        dp[i][j] = (dp[i-1][j-1] + dp[i][j-1] + dp[i-1][j]) % div
print(dp[n][m] % div)
```
### 2470 - 두 용액
- 이 문제를 풀 때에 실수 했던 부분은 오름차순 정렬을 한 리스트 liq에 대해서 두 포인터인 l, r의 값을 만약 현재 합이 음수일 경우에는 값을 늘려야 하기 때문에 l을 오른쪽으로, 합이 양수일 경우에는 값을 줄여야 하므로 r을 왼쪽으로 이동시켜야 하는 것을 헷갈려서 제출한 것이다.
```py3
# 2470 - 두 용액

# 같은 양의 두 용액을 혼합한 용액의 특성값은 혼합에 사용된 각 용액의 특성값의 합으로 정의
# 같은 양의 두 용액을 혼합하여 특성값이 0에 가장 가까운 용액을 만들고자 한다. (산성은 음, 연기성은 양)
# 두 개의 서로 다른 용액을 혼합할 때 특성값이 0에 가장 가까운 용액을 만들자

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

n = int(input())
liq = [-100000000001] + list(map(int, input().split()))

liq.sort()
currAns, currArr = abs(liq[1] + liq[n]), [liq[1], liq[n]]
if n == 2:
    for i in liq[1:]:
        print(i, end = ' ')
    exit(0)

s, y = [], []
for i in range(1,n+1):
    if (liq[i] < 0):
        s.append(liq[i])
    else:
        y.append(liq[i])

# 산성은 내림차순 염기는 오름차순 정렬
s.sort(reverse = True)
y.sort()
minS, minY = 2000000001, 2000000001
# 산성끼리
if (len(s) >= 2):
    minS = abs(s[-2] + s[-1])
# 염기끼리
if (n-len(s) >= 2):
    minY = (y[0]+y[1])

# 두개 섞어서
l,r = 1, n
if minS == min(minS, minY):
    currAns = minS
    currArr = (s[-1],s[-2])
else:
    currAns = minY
    currArr = (y[0], y[1])

while (1 <= l < r <= n):
    added = liq[l] + liq[r]
    if (added < 0):
        if (abs(added) < currAns):
            currAns = abs(added)
            currArr = [liq[l], liq[r]]
            l += 1
        else:
            l += 1
    elif (added > 0):
        if added < currAns:
            currAns = added
            currArr = [liq[l], liq[r]]
            r -= 1
        else:
            r -=1
    else:
        print(liq[l], liq[r])
        exit(0)
for i in currArr:
    print(i, end = ' ')
```
#### 12865 - 평범한 배낭
```py3
# 12865 - 평범한 배낭
# knapsack problem의 한 예시이다.     
# 여행에 필요하다고 생각하는 n개의 물건이 있을 떄 무게 w와 가치 v를 갖는다.
# 최대 k만큼의 무게만을 넣을 수 있는 배낭을 들고 다닐 때 물건들의 가치의 최댓값을 출력하여라

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

# dp[i][j] = 현재 idx번째 물건을 고려할 때에 대해서 최대 j만큼의 무게를 담을 때에 들 수 있는 가치의 최대이다.
# 만약 현재 idx의 물건의 무게가 j 이하라면 dp[i][j] = max(dp[(idx+1)%2][j-arr[idx][0]]+arr[idx][1], dp[(idx+1)%2][j])
# 만약 현재 idx의 물건의 무게가 j 초과라면 dp[i][j] = dp[(idx+1)%2][j]이다.
# 현재 idx의 무게를 사용할 수 없기 때문이고, 애초에 dp리스트에 저장된 값은 해당 조건에서의 가치의 최대이기 때문이다.

dp = [[0]*(k+1) for _ in range(2)]

for idx in range(n):
    i = idx%2
    for j in range(1, k+1):
        if (j>=arr[idx][0]):
            dp[i][j] = max(dp[(idx+1)%2][j-arr[idx][0]] + arr[idx][1], dp[(idx+1)%2][j])
        else:
            dp[i][j] = dp[(idx+1)%2][j]

print((dp[(n-1)%2][-1]))

# dynamic programming문제들의 경우, 우리가 구하고자 하는 출력값을 dp리스트에 저장되도록 하는 것을 잊지 말자
```

#### 2343 - 기타레슨
```py3
# 2343 - 기타 레슨
# 블루레이에 총 n개의 레슨을 넣을 수 있고, 순서가 바쒸면 안된다.
# 즉 i번 레슨과 j번 레슨을 같은 블루레이에 녹화하려면 i번, j번 사이의 모든 레슨도 같은 블루레이에 녹화 해야 한다.
# m개의 같은 크기의 블루레이를 이용한닥 한다.
# 가능한 m의 최솟값을 구해보자.

import sys, math
input = sys.stdin.readline

n, m = map(int, input().split()) # (1 <= n<= 1000000, 1 <= m <= n)
arr = list(map(int, input().split())) # 각 레슨의 길이

l, r = max(arr), sum(arr) # l의 값은 반드시 전체 용량의 최대여야 함. 모든 파일을 담을 수 있어야 하는 최소의 크기이기 때문이다.

# 예측하는 가능한 size의 값으로 블루레이 용량을 설정 할 때에 필요한 블루레이의 개수를 구하는 check(size) 함수
def check(size):
    count, add = 0, 0
    for i in range(n):
        if (add + arr[i] > size):
            add = 0
            count += 1
        add += arr[i]  
        # 이렇게 더해주어야 하는 이유는 add + arr[i]의 값이 size보다 크지 않을 때에도 갱신은 해 주어야 하기 때문
    if (add > 0):
        # add > 0이면 고려를 안해준 수업 파일이 있다는 의미이기 때문에 필요한 블루레이의 개수가 하나 늘어난다는 의미이다.
        count += 1
    return count

while (l <= r):
    mid = (l+r)//2
    if (check(mid) <= m):
        # check(mid)를 통해 구한 필요한 블루레이의 개수가 제한 값보다 작거나 같다면
        # 최대 용량이 더 작아도 된다는 이미이다. (반드시 작아야만 하는 것은 아님. -> 이게 check(mid)==m일 때 멈추어서는 안되는 이유이다.)
        r = mid - 1
    elif (check(mid) > m):
        # 예상하는 최대 용량을 키워야 함
        l = mid + 1

print(l)  # print(math.ceil((l+r)/2))를 해도 정답처리가 된다.

# l > r 일때 while문을 탈출하는 상황이기 때문에 l이 결국에는 파일을 담으려는 최소가 된다.
# 그리고 예를 들면 r = mid-1 = l이었는데 이러면 mid = mid-1이 된다.
# 그러면 r = mid-2가 된다면 l은 여전히 mid-1이고, 결국 이는 반복문 탈출시의 mid값을 출력하는 것이나 마찬가지라고 봐도 된다.
# 그러나 mid값과 계속 갱신을 하게 되면 2로 나누어 떨어지지 않을 떄 반례가 생기니 그렇게 하면 안된다. 
```