#### BOJ 2847 - 게임을 만든 동준이
1. 수열의 수를 하나 선택하여 1씩 감소시킬 수 있을 때, 증가수열(오름차순 정렬)이 되도록 하는 최소의 감소 횟수를 구하자
2. 감소 연산만 사용할 수 있다는 것이 핵심

```py3
import sys

n = int(sys.stdin.readline())
nums = []
for i in range(n):nums.append(int(sys.stdin.readline()))

answer = 0
big = nums[-1]
for i in range(n-2, -1, -1):
    while nums[i] >= big:
        answer += 1
        nums[i] -= 1
    big = nums[i]

print(answer)
```

**그리디를 사용했음에 대한 정당성 부여**
1. 만약 이 문제에서의 각 문제별 

#### BOJ 20044 - Project Teams
- 오름차순으로 정렬을 했는데 정렬을 할 때 sort() 대신에 버블 정렬을 사용해 보았는데 오히려 시간이 더 오래 걸렸다.
```py3
import sys

num = int(sys.stdin.readline())
n = num*2
score = list(map(int, sys.stdin.readline().split()))

for i in range(n-1, -1, -1):
    for j in range(i):
        if score[j] > score[j+1]:
            temp = score[j+1]
            score[j+1] = score[j]
            score[j] = temp

answer = 200001
for i in range(num):
    answer = min(answer, score[i] + score[2*num-i-1])

print(answer)
```

#### BOJ 16206 - 롤케이크
- 10의 배수인 길이의 자른 횟수 대비 나올 수 있는 조각의 효율이 더 좋기 때문에 10의 배수인 것을 먼저 처리할 수 있도록 하는 부분에서 그리디 알고리즘이 이용이 된다.
- 10의 배수인 길이와 아닌 길이를 따로 리스트에 나누어서 몫을 저장한 뒤에 10의 배수들의 경우에는 1을 뺀 값을 m에서 빼고 여기서 남은 m보다 작은 경우에는 정답에 m을 더한다.
- 이는 m이 0이 될 때까지 진행한다.
```py3
import sys

n,m = map(int, sys.stdin.readline().split())
length = list(map(int, sys.stdin.readline().split()))

ten, noten = [],[]
for i in length:
    if i % 10 == 0:
        ten.append(i//10)
    else:
        noten.append(i//10)

ten, noten = sorted(ten), sorted(noten)
answer = 0
for i in ten:
    if m == 0:
        break
    if m >= (i-1):
        m -= (i-1)
        answer += i
    else:
        answer += m
        m = 0
if m > 0:
    for i in noten:
        if m == 0:
            break
        if m >= i:
            m -= i
            answer += i
        else:
            answer += m
            m = 0

print(answer)
```

#### BOJ 4796 - 캠핑
- 캠핑장을 연속하는 p일 중에서 l일동안만 사용할 수 있다. v일동안의 휴가가 시작됬다면, 캠핑장은 최대 며칠동안 사용이 가능할까?
- 결국에는 정말 간단한 문제였다. 단순하게 몫과 나머지를 이용하면 되는 문제였는데, 마지막에 v를 p로 나누었을 떄의 나머지가 l보다 큰 경우에는 v를 p로 나눈 나머지가 아닌 l을 더해 주어야 한다.
- 이 부분만 해결하면 코드를 짜는 것은 함수와 while문을 이용하면 깔끔하게 해결이 가능하다.
```py3
import sys

def solution(l,p,v):
    if (v%p) < l:
        return (v//p)*l + (v%p)
    else:
        return (v//p)*l + l

index = 0
while True:
    index += 1
    l,p,v = map(int, sys.stdin.readline().split())
    if (l == p == v == 0):
        break
    else:
        answer = solution(l,p,v)
        print("Case "+str(index)+': '+str(answer))
```
#### BOJ 1080 - 행렬
- 행렬 A,B는 각각 0과 1로만 이루어져 있으며 문제는 행렬 A를 행렬 B로 바꾸는데 필요한 연산의 횟수의 최솟값을 구하라고 요구한다.
- 행렬의 크기는 각각 n,m이며 두 행렬 A,B의 크기는 같다.
- 만약에 A를 B로 바꿀 수 없다면 -1을 출력해야 한다.
- 탐욕법을 이용해서 푸는 문제인줄 몰랐으면 아마 해결을 못했을 것 같다. 
- 결국에는 답을 내는 함수 solution, 정답을 내기 위해서 순서대로 두 행렬의 칸을 같게 만들어 나가는 answer 함수, 그리고 check 행렬을 갱신하는 change 함수 3개를 구성했다.
- 두 행렬 a,b,가 주어졌을때 각 칸의 수가 같으면 1, 다르면 0을 해준다. 3x3 크기씩 뒤집어 주고 다 뒤집었을 때 전부 1이면 뒤집은 횟수를 출력하고 0이 있다면 -1을 출력한다. n과 m이 3보다 작다면 따로 예외적으로 0이 있으면 -1을, 없으면 0을 출력한다.
- 한 번 지나간 기준점은 더 이상 바뀔 일이 없게 되며 이후 비교에 영향을 주지 않는다.
```py3
import sys

n,m = map(int, sys.stdin.readline().split())
a,b = [],[]

for _ in range(n):
    a.append(list(map(int, sys.stdin.readline().strip())))
for _ in range(n):
    b.append(list(map(int, sys.stdin.readline().strip())))

count = 0

def change(nums, index):
    x,y = index[0], index[1]
    for i in range(x, x+3):
        for j in range(y, y+3):
            if nums[i][j] == 0:
                nums[i][j] = 1
            else:
                nums[i][j] = 0

def answer(n,m, check):
    global count
    for i in range(n-2):
        for j in range(m-2):
            if j == m-3:
                if sum(check[i][j:j+3]) == 0 or sum(check[i][j:j+3]) == 3:
                    if check[i][j] == 0:
                        count += 1
                        change(check, [i,j])
                    else:continue
                else:
                    return -1
            else:
                if check[i][j] == 0:
                    count += 1
                    change(check, [i,j])
                else:continue
    for i in range(n-2, n):
        for j in range(m):
            if check[i][j] == 0:
                return -1
    return count
        
            
def solution(n,m):
    if (n<3 or m<3):
        if a != b:return -1
        else:return 0
    else:
        check = [[0]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if a[i][j] == b[i][j]:
                    check[i][j] = 1
        return answer(n,m, check)

print(solution(n,m))
```

#### 2839 - 설탕 배달
- 5로 n이 나누어 떨어지는 경우는 무조건 5로 나눈 몫이 답이 될 것이고, 총 나눌 수 있는 최대의 횟수는 3으로 나눈 몫일 것이기 때문에 이를 for문을 이용해서 계산해 주면 된다.
```py3
import sys
n = int(sys.stdin.readline())
results = []

if n%5 == 0:
    results.append(n//5)
elif n%3 == 0:
    results.append(n//3)

trys = n//3+1
for i in range(trys):
    temp = n-(3*i)
    if temp%5 == 0:
        results.append(i+temp//5)
            
def solution(results):
    if results:
        print(min(results))
    else:
        print(-1)
        
solution(results)
```
#### 19639 - 배틀로얄
- recursion limit의 제한을 늘려주지 않았기 때문에 계속 런타임 에러가 발생했지만, 그 부분만 해결해 주니 맞았다고 나왔다.
- 그러나 문제는 시간이 4636ms로 생각보다 오래 걸렸다는 점이다.(시간문제는 개선할 필요가 있을 것 같다.)
- 결국에는 greedy algorithm이 적용된 부분이 적을 맞서는 것을 먼저 계산해서 처리해 주는 방법을 이용해서 회복 점수는 남으면 나중에 한꺼번에 처리해 주는 방법으로 해결을 했다. 
```py3
import sys

x,y,m = map(int, sys.stdin.readline().split())
loose, add = [],[]
l,a = 0,0
if x > 0:
    for i in range(x):
        loose.append([int(sys.stdin.readline())*-1, i+1])
        l += loose[i][0]
if y > 0:
    for i in range(y):
        add.append([int(sys.stdin.readline()), i+1])
        a += add[i][0]

loose_sort = sorted(loose)
add_sort = sorted(add, reverse=True)
answer = []

def calc(m):
    global answer,loose_sort, add_sort
    if loose_sort:
        l = loose_sort[0][0]
        if m+l> 0:
            answer.append(loose_sort[0][1]*-1)
            loose_sort.pop(0)
            calc(m+l)
        else:
            if add_sort:
                a = add_sort[0][0]
                answer.append(add_sort[0][1])
                add_sort.pop(0)
                calc(m+a)
            else:
                answer = []
                return
    else:
        if add_sort:
            for k in add_sort:
                answer.append(k[1])

def solution(m):
    global loose, add, answer
    if m+l+a <= 0:
        print(0)
    else:
        calc(m)
        if answer:
            for i in answer:
                print(i)
        else:
            print(0)
        
solution(m)
```
#### BOJ - 12931 - 두 배 더하기
```py3
import sys

n = int(sys.stdin.readline())
B = list(map(int, sys.stdin.readline().split()))

answer = 0
def solution(B):
    global answer
    if sum(B) == 0:
        return
    elif sum(list(map(lambda x: 0 if x%2 == 0 else 1, B))) == 0:
        answer += 1
        solution(list(map(lambda x:x//2,B)))
    else:
        for i in range(len(B)):
            if B[i] % 2 != 0:
                B[i] -= 1
                answer += 1
                solution(B)

solution(B)
print(answer)
```
#### BOJ - 13904 - 과제
```py3
import sys

n = int(sys.stdin.readline())
data = []
for i in range(n):
    data.append(list(map(int, sys.stdin.readline().split())))

data = sorted(data,key = lambda x:(x[1], x[0]))

result = [0]*1001

for i in range(n-1, -1,-1):
    if (result[data[i][0]] == 0):
        result[data[i][0]] = data[i][1]
    else:
        index = data[i][0]
        while (index >= 1):
            if (result[index] == 0):
                result[index] = data[i][1]
                break
            index -= 1

maxScore = sum(result)
print(maxScore)
```
