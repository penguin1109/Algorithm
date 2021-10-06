- '가장 큰 순서대로', '가장 작은 순서대로' 등의 키워드에 주목
#### 1. 거스름돈 문제
```py3
N = int(input())
mon = [500, 100, 50, 10]
ans = 0

for i, val in enumerate(mon):
    while val <= N:
        N -= val
        ans += 1
print(ans)
```
#### 2. 프로그래머스 - 체육복
```py3
def solution(n, lost, reserve):
    def check(val):
        if 0 <= val < n:
            return True
        return False
    answer = 0
    lost.sort()
    reserve.sort()
    
    clt = [1 for i in range(n)]
    
    for i in range(1, n+1):
        if (i in lost):
            clt[i-1] -= 1
        if (i in reserve):
            clt[i-1] += 1
    
    for i, val in enumerate(clt):
        if (val == 2):
            a, b = i-1, i+1
            if check(a) and clt[a] == 0:
                clt[a] += 1
                clt[i] -= 1
            elif check(b) and clt[b] == 0:
                clt[b] += 1
                clt[i] -= 1
    for i in clt:
        if i > 0:
            answer += 1
    # 여벌이 남아있는 사람이 분명 여전히 있을텐데 그 부분을 고려해 주지 않고 그냥 sum(clt)를 했다.
    return answer
```
#### 3. 큰 수의 법칙
- Sol01
```py3
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split()) # n -> 배열의 크기 m -> 숫자가 더해지는 횟수 
# 주어진 수들을 m번 더해서 배열의 특정 index가 k번 이상 더해지지 않아서 만들 수 있는 제일 큰 수를 구하여라

nums = list(map(int, input().split()))

answer = 0
nums.sort(reverse = True)
fir, sec = nums[0], nums[1]
# 이럴 때에 while 문을 사용하게 되면 오히려 실수를 할 가능성이 커질 것임
# 그냥 for문을 사용하는 것이 낫겠다.
# 연속으로 k번을 넘게 더해주는 것이 방지되어 있는 상황이기 때문에 제일 큰 수를 k번 더해준 뒤에 제일 작은 수를 한번씩 더해주는 과정을 m이 0이 될 때까지 반복해 주면 된다.

while True:
    for i in range(k):
        if m == 0:
            break
        answer += fir
        m -= 1
    if m == 0:
        break
    answer += sec
    m -= 1 # 이런데서 실수하지 말것 -> m에서 1을 더 빼 주어야 한다.
print(answer)
```
- Sol 02
- 시간 초과가 발생하지 않도록 하기 위해서 **반복되는 수열의 규칙성**을 발견할 필요가 있다.
- 쉽게 알수 있겠지만 제일 큰수 k번, 두번째로 큰 수 1번의 수열이 반복될 것이고 m을 (k+1)로 나눈 횟수만큼 반복될 것이다. -> 따라서 이런 식으로 몫과 나머지를 이용해 간단하게 해결이 가능하다.
```py3
import sys
input = sys.stdin.readline

n, m, k = map(int, input().split()) # n -> 배열의 크기 m -> 숫자가 더해지는 횟수 
# 주어진 수들을 m번 더해서 배열의 특정 index가 k번 이상 더해지지 않아서 만들 수 있는 제일 큰 수를 구하여라

nums = list(map(int, input().split()))

answer = 0
nums.sort(reverse = True)
fir, sec = nums[0], nums[1]

rep, more = m//(k+1), m%(k+1)

answer = (fir*k+sec) * rep + fir * more

print(answer)
```
#### 4. 프로그래머스 - 큰 수 만들기
```py3

```

<<<<<<< HEAD
#### 5. 프로그래머스 - 조이스틱 (dfs)로 해결해야 하는 문제였던 것인가...! 
=======
#### 5. 1로 만들기
- 시간 초과를 줄이기 위한 효과적인 방법 -> 어차피 k로 나누어 떨어지지 않으면 그 이후로는 남은수의 1뺀 값만 더하면 된다.
- 따라서 그냥 k만큼 나누었을 때에 최대로 나눌 수 있는 방법을 먼저 구하면 된다.
```py3
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
answer = 0
while True:
    target = (n//k)*k 
    answer += (n-target)
    n = target
    if (n < k):
        break
    answer += 1
    n //= k

answer += (n-1) # 1이 될때까지 1만큼 빼 줄 것이기 때문에 해당 부분 계산

print(answer)
```
#### 백준 - 1439. 문자열 뒤집기
- 시간 76ms
```py3
import sys
input = sys.stdin.readline

# 0과 1로만 이루어진 문자열
# 문자열을 모두 같은 수로 만들기 위한 최소의 뒤집는 횟수

q = list(map(int, input().strip()))
zeros, ones = 0,0

while q:
    curr = q.pop()
    if curr == 0:
        zeros += 1
    else:
        ones += 1
    while (q and q[-1] == curr):
        q.pop()
print(min(zeros, ones))
```
>>>>>>> 166c12fb63db4b9f03e68b83844a0c12ea765459
