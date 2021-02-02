## PREFIX SUM &  TWO POINTERS

#### BOJ 11659 - 구간합 구하기 4
- 구간 [0, j]까지의 원소의 합을 pre[j]라고 정의하면, 구간 [i, j]의 합은 sums[j] - sums[i-1]이다.
  
```py3
# 11659 - 구간 합 구하기 4
# 수 n개가 주어졌을 때, i번째 수부터 j번째 수까지의 합을 구하는 프로그램을 작성하시오

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

n, m = map(int, input().split()) # 1 <= n,m <= 100000
sums = [0]*(n+1)
nums = list(map(int, input().split())) # 1000보다 작거나 같은 자연수
for i in range(1, n+1):
    sums[i] = nums[i-1] + sums[i-1]

for _ in range(m):
    i,j = map(int, input().split())
    print(sums[j] - sums[i-1])
```

#### BOJ 11660 - 구간합 구하기 5
- answer = sums[x2][y2] - sums[x1-1][y2] - sums[x2][y1-1] + sums[x1-1][y1-1]
```py3
# 11659 - 구간 합 구하기 5
# NxN개의 수가 NxN 크기의 표에 채워져 있을 떄에 m개의 줄에 4개의 정수 x1,y1,x2,y2가 주어지면
# (x1, y1)부터 (x2, y2)의 합을 출력

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

n, m = map(int, input().split()) # 1 <= n <= 1024, 1 <= m <= 100000

sums = [[0]*(n+1) for _ in range(n+1)] # sums[i][j]는 주어지는 숫자 표의 (i,j)부터 (0,0)까지의 합
nums = [list(map(int, input().split())) for _ in range(n)] # 1000보다 작거나 같은 자연수

# sums 2차원 리스트 채워주기
for i in range(1,n+1):
    for j in range(1, n+1):
        # 포함 배제의 원리 적용
        # 중복된 부분 빼주고 새로운 숫자 더해주기
        sums[i][j] = sums[i][j-1] + sums[i-1][j] - sums[i-1][j-1] + nums[i-1][j-1]

# 구간의 합 구해주기 (마찬가지로 포함 배제의 원리 적용)
for _ in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    print(sums[x2][y2] - sums[x1-1][y2] - sums[x2][y1-1] + sums[x1-1][y1-1])
```

#### 2003 - 수들의 합 2
- 수열의 첫번째 수를 모두 index로 설정해 준다.
- l, r의 두개의 포인터 중에서 만약에 현재 l에서 r까지의 구간합이 m이라면 answer += 1을 해주고 m보다 클 떄에는 l += 1, 작을 떄에는 r += 1
- 만약에 r이 범위 n을 넘어간다면 break를 해준다.
  - 이는 r이 만약에 이동할 수 있을 때 l은 당연히 n보다 작을 것이라는 정당성이 증명이 되기 떄문에 r의 크기만 조절해 주면 되는 것이다.
  
```py3
# 2003 - 수들의 합 2
# n개의 수로 이루어진 수열 A를 이용할 때에 수열의 i번째 부터 j번째까지의 합이 m이되는 경우의 수를 구하자

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

n, m = map(int, input().split()) # 1 <= n <= 10000, 1 <= m <= 300000000
nums = list(map(int, input().split()))
answer = 0
temp = 0
l, r = 0, 0

while True:
    if (temp >= m):
        temp -= nums[l]
        l += 1
    elif (r == n):
        break
    else:
        temp += nums[r]
        r += 1
    if (temp == m):
        answer += 1

print(answer)
```

#### 1484 - 다이어트
- 먼저 모든 제곱수를 주어지는 제곱수들의 차이 G보다 큰 값까지 저장된 배열 arr을 만들어준다.
- 처음에는 제곱수들의 차를 구해서 전부 더하는 방법을 사용할까 했지만 실수가 발견되는 것 같아서 우선은 그냥 모든 제곱수를 저장하고 차를 그때 그떄 구했다.
  - 이는 직접 해보니 제곱수의 크기가 증가할 수록 차이의 크기도 증가하기 때문에 가능하다.
  - 따라서 투 포인터를 응용해서 해당 차가 G보다 크면 l += 1, G 보다 작으면 r += 1, G와 같으면 answer에 값을 넣고 r += 1
  - 당연히 arr[l] < arr[r]인데 처음에는 반대로 차를 구해주어서 계속 답이 -1이 나오는 실수를 저질렀었다.

```py3
# 1484 - 다이어트
# 첫째 줄에 G가 주어진다.
# G는 현재 몸무게의 제곱에서 기억하고 있던 무게를 뺀 값이다.
# 첫째 줄부터 한 줄에 하나씩 가능한 현재 몸무게를 오름차순으로 출력하고 존재하지 않을 떄는 -1을 출력한다.
# 몸무게가 자연수로 나누어 떨어지지 않을 떄는 제외

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

G = int(input()) # 1 <= G <= 100000

if (G%2 == 0):
    last = (G//2)
else:
    last = (G+1)//2

arr = [0]*(last+1)
for i in range(last+1):
    arr[i] = (i+1)**2

l, r = 0, 0
answer = []

while (True):
    if (r >= last+1):
        break
    temp = arr[r] - arr[l]
    if (temp > G):
        l += 1
    elif (temp < G):
        r += 1
    elif (temp == G):
        answer.append(int(arr[r]**0.5))
        r += 1

if (answer):
    for k in answer:
        print(k)
else:
    print(-1)
```

#### 1253 - 좋다
- Naive하게 모든 경우를 2중 for문을 사용해서 따져보아도 되는 것이지만 그렇게 하면 너무 시간 복잡도가 커질 것이 분명하기 때문에 
- 투 포인터 알고리즘을 사용하여야 한다.
- 음의 정수도 존재하기 떄문에 두 포인터를 각각 배열의 첫, 마지막 index로 설정해 주어야 한다.
- 수열의 모든 수들을 각각 좋은 수인지 아닌지 검증하는 과정을 한번씩 거쳐야 한다.
- 투 포인터를 이용해서 좋은 수로 판별하려는 수가 더 크다면 l += 1, 더 작다면 r -= 1을 해준다.
- 서로 다른 수를 이용해서 구해주는 것이기 떄문에 l < r일 동안에 while 반복문을 돌려 주어야 하고, 또한 합이 현재 좋은수 여부를 확인하는 수와 같다면
  1. l != i && r != i이면 arr[i] = 1, break를
  2. 아니라면 l != r임은 보장이 되어 있으므로 둘 중 하나만 i일 것이기 떄문에 l == i일 때는 l += 1, r == i일 때는 r -= 1을 해준다.
   
```py3
# 1253 - 좋다
# N개의 수 중에서 어떤 수가 다른 수 두 개의 합으로 나타낼 수 있다면 그 수를 '좋다'고 한다.
# N개의 수가 주어지면 그 중에서 좋은 수의 개수는 몇 개인지 출력하라
# 수의 위치가 다르면 값이 같아도 다른 수이다.

# 주의! 서로 다른 수가 아니라 검증하고자 하는 수와 달라야 한다.(이때 다른 자리이면 다른 수로 간주)
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

n = int(input()) # 1 <= n <= 2000
nums = list(map(int, input().split())) # 절댓값이 1000000000이하의 정수로 구성
nums.sort()

arr = [0] * n

for i in range(n):
    check = nums[i]
    l, r = 0, n-1
    while (l < r):
        if (nums[l] + nums[r] > check):
            r -= 1
        elif (nums[l] + nums[r] < check):
            l += 1
        else:
            if (l != i and r != i):
                arr[i] = 1
                break  
            elif l == i:
                l += 1
            elif r == i:
                r -= 1
print(sum(arr))
```

## 스택, 큐, 덱

#### 4949 - 균형 잡힌 세상
```py3

```
#### 1935 - 후위 표기식2
```py3
# 1935 - 후위 표기식2
# 후위 표기식과 각 피연산자에 대응하는 값들이 주어질 때 그 식을 계산하는 프로그램을 작성하시오
# 계산 결과를 소숫점 둘째 자리까지 출력한다.

import sys, string
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

alpha = list(string.ascii_uppercase) # 대문자 알파벳이 모두 담긴 리스트

n = int(input()) # 1 <= n <= 26
arr = list(str(input())) # 계산해야 하는 계산식
nums = [int(input()) for _ in range(n)] # A부터 n번째 알파벳까지 순서대로 대응되는 숫자값

data = dict()
for i in range(n):
    data[alpha[i]] = nums[i]

temp = []

while arr:
    curr = arr.pop(0)
    if (curr in alpha):
        temp.append(data[curr])
    else:
        if len(temp) >= 2:
            a,b = temp.pop(), temp.pop()
            #print(a,b)
            if curr == '+':
                temp.append(a+b)
            elif curr == '*':
                temp.append(a*b)
            elif curr == '/':
                temp.append(b/a)
            else:
                temp.append(b-a)
        if (len(temp) == 1 and len(arr) == 0):
            print('%0.2f' %temp[0])
            exit(0)
```

#### 4949 - 균형잡힌 세상
- input = sys.stdin.readline으로 하면 readline을 사용하면 뒤에 '\n'이 붙기 때문에 그렇게 해결하면 안되는 것이다.
- 그래서 그냥 input()으로 입력 받았더니 출력초과가 발생하지 않았다.
```py3
# 4949 - 균형잡힌 세상

import sys, string

valid = list('()[]'.strip())
def check(inputs):
    temp = []
    while inputs:
        curr = inputs.pop(0)
        if temp:
            a = temp.pop()
            if (curr == ')'):
                if (a != '('):
                    return False
            elif (curr == ']'):
                if (a != '['):
                    return False
            elif (curr == '[' or curr == '('):
                temp.append(a)
                temp.append(curr)
            else:
                temp.append(a)
        else:
            if (curr in valid):
                temp.append(curr)
    if (temp):
        return False
    else:
        return True
            
while True:
    a = list(input())
    if a == ['.']:
        break
    else:
        if check(a):
            print('yes')
        else:
            print('no')
```            
#### 1158 - 요세푸스 문제
- 처음에 그냥 list를 이용해서 arr.pop(0)을 해 주었더니 시간 초과가 python3, pypy3 모두에서 발생했다.
- 그러나 from collections import deque 모듈을 사용해 주었더니 해결이 되었다.
- 이는 deque의 pop(0)이 아닌 popleft()라는 함수가 적용이 될 수 있기 때문이라고 생각한다.
- 출력 형식에 대괄호가 있기 때문에 해당 순서의 수를 찾을 때 마다 출력하는 것이 편할 것이라 생각하여서 현재까지의 count가 k일때 출력, 아니면 append를 이용했고, k일때에도 현재 arr이 비어있으면 exit(0), 비어 있지 않다면 count = 0으로 다시 초기화
```py3
# 1158 - 요세푸스 문제
# 1번부터 n번까지 n명의 사람이 원을 이루며 앉아 있고 양의 정수 k가 주어진다.
# 순서대로 k번째 사람을 제거하는데, 한 사람이 제거되면 남은 사람들로 이루어진 원을 따라 이 과정을 반복하게 된다.
# 원에서 사람들이 제거되는 순서인 요세푸스 순열을 구하여라

import sys
input = sys.stdin.readline
from collections import deque

n, k = map(int, input().split()) # 1 <= k <= n <= 5000
arr = deque(list(int(i) for i in range(1, n+1)))

count = 0
print('<', end = '')
while arr:
    a = arr.popleft()
    count += 1
    if (count == k):
        if (arr):
            print(str(a) + ', ', end = '')
        else:
            print(str(a) + '>', end = '')
            exit(0)
        count = 0
    else:
        arr.append(a)
```
- 파이썬에서 배열의 크기가 증가하거나 index값이 작은 부분에 삽입/삭제가 일어날 경우 비효율적이기 떄문에 이럴 때에 collections.deque를 사용하자
- deque는 내부적으로 doubly-linked-list로 표현이 된다. 따라서 양 끝단에 모두 접근이 가능하지만 deque의 가운데 부분을 찾거나 중간에 삽입, 제거하는 것은 느리다.

#### 1966 - 프린터 큐
- 저번에 했을 때는 시간이 180ms가 나왔는데 이번에는 시간이 84ms로 절반보다 줄었기 때문에 풀고 난 이후 매우 뿌듯했던 문제이다.
```py3
# 1966 - 프린터 큐
# 현재 큐의 가장 앞에 있는 문서의 중요도를 확인
# 나머지 문서들 중 현재 문서보다 중요도가 높은 문서가 아니라 하나라도 있다면 이 문서를 인쇄하지 않고 큐의 가장 뒤에 재배치한다.
# 그렇지 않으면 바로 인쇄를 한다.
# 각 테스트 케이스에 대해 문서가 몇 번째로 인쇄되는지 출력한다.

import sys
input = sys.stdin.readline
from collections import deque

def order(n,m,impt):
    arr = deque(list(int(i) for i in range(n)))
    sorted_impt = deque(sorted(impt))
    count = 1
    while (arr):
        a = arr.popleft()
        if (impt[a] == sorted_impt[-1]):
            if (a != m):
                sorted_impt.pop()
                count += 1
            if (a == m):
                print(count)
                return
        else:
            arr.append(a)
    



t = int(input())     # t = number of testcases
for _ in range(t):
    n, m = map(int, input().split()) # n = 문서의 개수 (1 <= n <= 100), m = 궁금한 문서가 현재 queue에서 몇 번째에 놓여있는지 (0 <= m < n)
    impt = list(map(int, input().split()))
    order(n,m,impt)
```

#### 1021 - 회전하는 큐
```py3
# 1021 - 회전하는 큐
# n개의 원소를 포함하는 양방향 순환 큐를 사용한다.
# 여기서 원소를 뽑아내고자 하는데 
# 1. 첫 번째 원소를 뽑는다.
# 2. 왼쪽으로 한 칸 이동 -> 첫번째 원소가 마지막 원소가 됨
# 3. 오른쪽으로 한 칸 이동 -> 마지막 원소가 첫번째 원소가 됨
# 현재 위치가 주어지는 원소를 뽑아내는데 드는 2번, 3번 연산의 최솟값은?

import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().split()) # n = 큐의 크기 (1 <= n <= 50, int) m = 뽑아내려는 수의 개수 (m <= n)
nums = list(map(int, input().split())) # 뽑아내려는 수 m개의 위치

def pop_left(deck): # 연산 2 - 앞에서 뽑아서 뒤에 붙이기
    global answer
    if deck:
        a = deck.pop(0)
        answer += 1
        deck.append(a)
        return deck

def pop_right(deck): # 연산 3 - 뒤에서 뽑아서 앞에 붙이기
    global answer
    if deck:
        a = [deck.pop()]
        answer += 1
        deck = a + deck
        return deck
answer = 0
deck = list(int(i) for i in range(1,n+1))

while nums:
    if nums[0] == deck[0]:
        deck.pop(0)
        nums.pop(0)
    else:
        if deck.index(nums[0]) <= len(deck) // 2:
            while deck[0] != nums[0]:
                deck = pop_left(deck)
        else:
            while deck[0] != nums[0]:
                deck = pop_right(deck)

print(answer)
```

#### 19591 - 독특한 계산기
```py3
# 19591 - 독특한 계산기
# 수식에서 맨 앞의 연산자, 또는 맨 뒤의 연산자 먼저 계산 (음수의 부호는 연산자로 취급 X)
# 곱셈, 나눗셈을 덧셈, 뺄셈보다 먼저 계산
# 연산자의 우선 순위가 같다면 해당 연산자 계산 시 큰 결과부터 계산
# 계산했을 때 결과 값도 같다면 앞의 것을 먼저 계산

from abc import ABCMeta
import sys, math
input = sys.stdin.readline
from collections import deque

deck = deque()
seq = deque(list(str(input()).strip()))

calc = ['+', '*', '-', '/']
A, B = [], [] # A는 숫자 B는 연산자

# 숫자 앞에 있는 불필요한 0을 제거해서 숫자를 담으려는 리스트 A에 넣어준다.
idx = 0
minus = False
while (idx < len(seq)):
    if seq[idx] in calc:
        if (idx == 0 and seq[idx] == '-'): # 첫번째 숫자로만 음수가 나올 수 있는데 이 경우를 고려해 주는 경우
            minus = True
            idx += 1
        else:
            B.append(seq[idx])
            idx += 1
    else:
        temp = ''
        while (seq[idx] not in calc):
            temp += seq[idx]
            temp = str(int(temp))
            idx += 1
            if (idx == len(seq)):
                break
        if minus:
            temp = '-' + temp
            minus = False
        A.append(temp)

impt = {'+' : 1, '*' : 2, '-' : 1, '/' : 2} # 연산자의 우선순위

if not B:
    print(A[0])
else:
    while (True):
        if len(A) == 1:
            print(A[0])
            break
        if len(A) == 2:
            print(eval(str(A[0]) + B[0] + str(A[1])))
            break

        a11,a12,a21,a22 = A[0],A[1], A[-1], A[-2] # 숫자 앞에서  2개 뒤에서 2개
        b1,b2 = B[0], B[-1] # 연산자 앞, 뒤 각각 하나씩
        if (impt[b1] == impt[b2]):
            temp1 = math.trunc(eval(str(a11) + b1 + str(a12)))
            temp2 = math.trunc(eval(str(a22) + b2 + str(a21)))
            if (temp1 >= temp2):
                A.pop(0)
                A.pop(0)
                B.pop(0)
                A = [temp1] + A
                temp = math.trunc(eval(str(A[-2]) + b2 + str(A[-1])))
                A.pop()
                A.pop()
                B.pop()
                A.append(temp)
            else:
                A.pop()
                A.pop()
                B.pop()
                A.append(temp2)
                temp = math.trunc(eval(str(A[0]) + b1 + str(A[1])))
                A.pop(0)
                A.pop(0)
                B.pop(0)
                A = [temp] + A

        else:  
            if (impt[b1] > impt[b2]):
                temp = math.trunc(eval(str(a11) + b1 + str(a12)))
                A.pop(0)
                A.pop(0)
                B.pop(0)
                A = [temp] + A
                temp = math.trunc(eval(str(a22) + b2 + str(a21)))
                A.pop()
                A.pop()
                B.pop()
                A.append(temp)
            else:
                temp = math.trunc(eval(str(a22) + b2 + str(a21)))
                A.pop()
                A.pop()
                B.pop()
                A.append(temp)
                temp = math.trunc(eval(str(a11) + b1 + str(a12)))
                A.pop(0)
                A.pop(0)
                B.pop(0)
                A = [temp] + A
```