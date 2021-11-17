#### 2225 - 합분해
- 0부터 N까지의 정수 K개를 더해서 합이 N이 되는 경우의 수를 구하여라
- 덧셈의 순서가 바뀐 경우는 다른 경우로 세며, 한 개의 수를 여러번 사용할 수 있다.
- 같은 경우를 어떻게 제거해야 하나 막막했지만 생각해 보니 모든 경우를 다 해보면 해결 될 문제였다.
```python
div =  1000000000
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
max_size = N*K+1
# dp[i][j]는 i개의 수를 사용할 때 합이 j인 경우의 수를 의미
# 중복 제거를 위해서 어떤 방법을 사용할지 -> 그냥 배열에 전부 넣거나 개수만 구하거나
dp = [[0 for _ in range(N+1)]for _ in range(K+1)]

for i in range(1, K+1):
    for j in range(N+1):
        if i == 1 and j <= N:
            dp[i][j] = 1
        elif i != 0:
            for k in range(j+1):
                dp[i][j] += dp[i-1][k]
print(dp[K][N]%div)
```

#### 9024 - 두 수의 합
- 여러개의 서로 다른 정수와 또 다른 정수 K가 주어질 때 서로 다른 정수들에 속하는 서로 다은 두개의 정수의 합이 K에 가장 가까운 두 정수를 구할 것
- 처음에는 combination을 사용했는데 메모리 초과가 발생함
- 그 다음에는 K와의 차이를 0부터 시작해서 점점 키워나가면서 solution 함수를 사용해 해당 차이를 보이는 합이 생길 수 있는지 확인하고 개수를 세도록 했는데 이 경우에는 시간 초과가 발생하였다.
- 그래서 결국 투포인터를 사용해서 만약에 K와의 차이가 현재 찾는 차이보다 작다면 m값을 갱신하는 방향으로 l이 r보다 작을 때까지 진행한다.
```python
def answer(K, nums):
    m = max(abs(K-nums[-1]*2), abs(K-nums[0]*2))
    count = 0
    l, r = 0, len(nums)-1
    while (l < r):
        a, b = nums[l], nums[r]
        if (a+b == K):
            l += 1
            r -= 1
        elif (a+b > K):
            r -= 1
        else:
            l += 1
        if (abs(K-(a+b)) < m):
            m = abs(K-(a+b))
            count = 1
        elif (abs(K-(a+b)) == m):
            count += 1
    return count
t = int(input())

for _ in range(t):
    n, K = map(int, input().split())
    nums = list(map(int, input().split()))
    nums.sort() # 오름차순 정렬
    print(answer(K, nums))
```

#### 2204 - 도비의 난독증 테스트
- 영어 단어들을 제시한 후 어떤 단어가 대소문자를 구분하지 않고 사전순으로 가장앞서는지 맞추자
- 계속 50%대에서 틀렸습니다라는 결과가 나와서 반례를 찾느라 고생했다.
- 대소문자를 구분하지 않는다고 한다.
```python
import sys
input = sys.stdin.readline
while True:
    n = int(input())
    if n == 0:
        break
    else:
        words = []
        for _ in range(n):
            w = (str(input()).strip())
            words.append(w)
        words.sort(key = lambda w:w.lower())
        print(words[0])
```


#### 프로그래머스 10주차 - 교점에 별 만들기
- Ax + By + C = 0으로 표현할 수 있는 n개의 직선이 주어질 때 이 직선의 교점 중 정수 좌표에 별을 그리고자 한다.
- 