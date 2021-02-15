## 02.03 스터디 - EDOC

#### 2504 - 괄호의 값
```py
# 2504 - 괼호의 값
# 주어진 괄호열을 읽고 그 괄호값을 앞에서 정의한대로 계산하여 출력할 수 있도록 한다.

import sys
input = sys.stdin.readline
from collections import deque

string = deque(list(str(input().strip())))

Open, Close = ['(', '['], [')', ']']

answer = 0
calc, nums = [], [] # 연산자 저장 리스트, 피연산자 저장 리스트
# 길이의 최댓값이 30으로 짧기 때문에 deque를 사용하기 보다는 그냥 리스트를 사용

while string: # 입력받은 문자열의 모든 수를 고려해 줄 수 있을 때까지
    a = string.popleft()
    if a in Open: # 열림연산에 의한 2, 3과 올바른 괄호열의 연산 결과에 의한 2,3 또는 nums의 수들을 구분해 주기 위해 음수를 붙임
        calc.append(a)
        if a == '(':
            nums.append(-2)
        else:
            nums.append(-3)
    elif a in Close:
        # 현재 닫힘 괄호와 짝이 맞는 열림 괄호가 나올 때 까지 while 반복문으로 nums에 있는 수들의 연산을 수행
        # 그 과정에서 만약에 올바른 괄호열이 될 수 없다면 0을 출력하고 sys.exit()으로 아얘 탈출한다.
        if a == ']':
            temp = 0 
            while True: 
                if len(nums) == 0: # 닫힘 괄호가 먼저 나와서 올바른 괄호열이 아닌 경우
                    print(0)
                    sys.exit()
                curr = nums.pop()
                if (curr > 0):
                    temp += curr
                elif (curr == -2): # 열림과 닫힘의 짝이 안 맞아서 올바른 괄호열이 아닌 경우
                    print(0)
                    sys.exit()
                elif (curr == -3): # 올바른 괄호열인 경우에 현재 닫힘 괄호와 짝이 맞는 열림 괄호를 찾은 경우 (음수로 구분해 놓음)
                    if temp == 0:
                        temp = 1
                    temp *= 3
                    nums.append(temp)
                    break
        else:
            temp = 0
            while True:
                if len(nums) == 0:
                    print(0)
                    sys.exit()
                curr = nums.pop()
                if (curr > 0):
                    temp += curr
                elif (curr == -3): # 올바른 괄호열이 아닌 경우
                    print(0)
                    sys.exit()
                elif (curr == -2): # 올바른 괄호열인 경우에 현재 닫힘 괄호와 짝이 맞는 열림 괄호를 찾은 경우
                    if temp == 0:
                        temp = 1
                    temp *= 2
                    nums.append(temp)
                    break

while len(nums) > 0:
    a = nums.pop()
    if (a < 0):
        print(0)
        sys.exit()
    else:
        answer += a
print(answer)
```

#### 10025 - 게으른 백곰
- 사실상 주어진 이동할 수 있는 거리인 K에서 2xK+1의 값이 제일 멀리있는 얼음의 위치보다 크다면 곰의 위치는 의미가 없다.
- 그렇기 때문에 크다면 그냥 모든 얼음의 합을 구해서 exit(0)을 해주면 되고, 만약에 작다면 각각의 위치에서의 처음부터의 전체 얼음의 양을 저장해준 뒤에 곰의 위치에 따라서 (k+1 <= position <= n-k-1)로 지정을 해서 부분합으로 curr = max(answer, arr[position+k] - arr[position-k-1]) 이런식으로 해주면 풀리는 문제이다.
```py
# 10025 - 게으른 백곰
# 택한 최적의 위치로부터 k만큼 떨어진 거리 내에 있는 얼음들의 합의 최댓값을 출력한다.

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)
from collections import deque

n, k = map(int, input().split())
ice = [list(map(int, input().split())) for _ in range(n)]
ice.sort(key = lambda x: x[1])

ices = [0]*(ice[-1][-1] + 1)
max_length = ice[-1][-1] # 최대 길이

for i in range(n):
    a, b = ice[i][0], ice[i][1]
    ices[b] = a # ices[b]는 b번째 위치에 저장된 얼음의 양이다.

board = deque()
max_ice, temp_ice = 0, 0 # 지금까지 최대로 수용 가능했던 얼음의 양, 현재 상황에서 수용 가능한 얼음의 양

for l in range(max_length+1):
    curr_ice = ices[l]
    if l < 2*k + 1:
        temp_ice += curr_ice
        board.append(curr_ice) # board리스트에는 북극곰이 위치를 이동한 것을 기록해 놓기 위해서 현재 위치(l)에서 수용 가능한 얼음의 양을 저장해 둔다.
        max_ice = max(max_ice, temp_ice)
    else:
        unavailable = board.popleft()
        temp_ice = temp_ice - unavailable + curr_ice
        max_ice = max(max_ice, temp_ice)
        board.append(curr_ice)
print(max_ice)
```

#### 17298 - 오큰수
- Sol1
```py
n = int(input())
num = list(map(int, input().split(' ')))
stack = []
ans = []
stack.append(num[-1])
for i in range(n-2, -1,-1):
    while stack and stack[-1] <= num[i]:
        temp = stack.pop()
    if stack:
        ans.append(stack[-1])
    else:
        ans.append(-1)
    stack.append(num[i])

ans = ans[::-1]
ans.append(-1)
for i in ans:
    print(i, end = ' ')
```
- Sol2
```py
# 17298 - 오큰수
# 크기가 n인 수열 A
# 오큰수 = A(i)의 오른쪽에 있으면서 A(i)보다 큰 수 중에서 가장 왼쪽에 있는 수 (그러한 수가 없다면 -1)

import sys
input = sys.stdin.readline

n = int(input()) # 수열의 크기 n (1 <= n <= 1000000)
A = list(map(int, input().split()))
arr = [[A[i], i] for i in range(n)]
answer = [-1]*n # 정답으로 출력할 리스트
stack = []
stack.append(0)
i = 1

while (stack and i < n):
    while (stack and A[i] > A[stack[-1]]):
        answer[stack[-1]] = A[i]
        stack.pop()
    stack.append(i)
    i += 1

for i in answer:
    print(i, end = ' ')
```

#### 17299 - 오등큰수
```py
# 17299 - 오등큰수
# 크기가 n인 수열 A에 대해서 수열의 각 원소에 대해서 오등큰수를 구하고자 한다.
# 각 수가 수열에서 등장한 횟수를 F(A(i))라고 할 때 오등큰수는 오른쪽에 있으면서 A에 등장한 횟수가 F(A(i))보다 큰 수 중 가장 왼쪽에 있는 수
#그런 수가 없으면 오등큰수는 -1이다.

import sys
input = sys.stdin.readline
from collections import deque, Counter

n = int(input()) # 수열 A의 크기 (1 <= n <= 1000000)
A = list(map(int, input().split()))
cnt = Counter(A)
count = dict()
for i in list(set(A)):
    count[i] = cnt[i]
stack = []
stack.append(0)
arr = list([cnt[i], i] for i in A)
answer = [-1] * n

i = 1
while (stack and i < n):
    # stack[-1]은 현재 수의 오른쪽에 있는 선택 될 수 있는 수중에서 가장 왼쪽에 있는 수이다.
    # 이는 stack의 First in Last out의 FILO특성에서 차용한 것이다.
    while (stack and arr[stack[-1]][0] < arr[i][0]):
        #print(stack)
        answer[stack[-1]] = arr[i][1]
        stack.pop()
    stack.append(i)
    i += 1
for i in answer:
    print(i, end = ' ')
# 가장 왼쪽에 있는 수를 찾으라는 것은 곧 가장 먼저 등장하는 수를 오등큰수로 결정하라는 의미
```

#### 20002 - 사과나무
- Python3와 PyPy3을 이용해서 똑같은 알고리즘을 이용해서 제출했는데 둘 다 시간초과가 났다.
- 그래서 그냥 C로 같은 알고리즘으로 제출했더니 훨씬 빨리 통과가 되었다.
- 역시 알고리즘을 풀 때에는 C인 것인가...
- 만약에 여기서 부분합을 dp[x][y] (1 <= x < n, 1 <= y < n)에 대해서 (0,0)부터 (x,y)까지의 정사각형에서의 부분합으로 정의한다면
  - arr[x][y] += arr[x-1][y] + arr[x][y-1] - arr[x-1][y-1]
```c
#include <stdio.h>
int main()
{
    int n;
    int orch[300][300];
    int dp[301][301];

    scanf("%d", &n);
    for (int i = 0;i<n;i++){
        for (int j = 0;j<n;j++){
            scanf("%d", &orch[i][j]);
        }
    }

    for (int i = 1; i<=n; i++){
        for (int j = 1; j <=n; j++){
            dp[i][j] = orch[i-1][j-1] + dp[i][j-1];
        }
    }

    long ans = -999999999;
    int length, i, j,k;
    for (length= 1; length <= n; length++){
        for (i = 1; i<=n-length+1;i++){
            for (j = 1; j<= n-length+1;j++){
                int add = 0;
                for (k = 0;k<length;k++){
                    add += (dp[i+k][j+length-1] - dp[i+k][j-1]);
                }
                if (add > ans){
                    ans = add;
                }
            }
        }
    }
    printf("%d", ans);
    return 0;
}

```