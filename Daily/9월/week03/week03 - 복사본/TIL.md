### 프로그래머스 - 8주차 weekly  
```python
# 최소 직사각형
# 모든 명함을 수납할 수 있는 가장 작은 지갑을 만들 때에 지갑의 크기를 return
import math
class Main():
    def check(self, cycle,w,h, sizes):
        global result
        if (cycle == len(sizes)):
            result.append(w*h)
            return
        else:
            W, H = sizes[cycle][0], sizes[cycle][1]
            self.check(cycle+1, max(w, W), max(h, H), sizes)
            self.check(cycle+1, max(w,H), max(h, W), sizes)

    def solution(self, sizes):
        """가로와 세로의 길이라고 제공해주는 것의 의미가 특별히 있는 상황이 아니기 때문에
        입력값을 비교해서 더 짧은 길이를 무조건 가로, 더 긴 길이를 세로로 설정해서
        각각의 가로와 세로에서 최댓값의 곱이 답이다"""
        big_w, big_h = 0,0
        for s in sizes:
            w, h = s[0], s[1]
            if w > h:
                s = [h, w]
            big_w = max(big_w, s[0])
            big_h = max(big_h, s[1])
        return big_w*big_h
        
    def solution01(self, sizes):
        """백트래킹과 재귀를 사용해서 모든 경우 탐색 -> 시간 초과 발생"""
        global result
        answer = math.inf
        self.check(0, 0, 0, sizes)
        return min(result)

main = Main()
sizes = [[[60, 50], [30, 70], [60, 30], [80, 40]],[[10, 7], [12, 3], [8, 15], [14, 7], [5, 15]],[[14, 4], [19, 6], [6, 16], [18, 7], [7, 11]]]
for s in sizes:
    result = []
    print(main.solution(s))
```

### BOJ - 16288. Passport Control
#### 처음에 계속 틀렸다고 한 이유
- YES, NO라고 출력하도록 해야 하는데 Yes, No로 출력하도록 했다.

#### 성공한 풀이
- Sol01
1. 총 사용이 가능한 출력창구의 개수가 k임을 사용해서 stack이라는 2차원 배열을 사용해서 각각의 창구에서 대기할 수 있는 사람을 넣는 용도로 사용하였다.
2. 만약에 현재 사용자가 각 창구의 가장 번호가 뒤인 사람보다 번호가 크다면 valid = True로 설정해 준다.
3. cycle만큼 반복문을 돈 뒤에 valid = True이면 각 창구마다 제일 번호가 큰 사람들중의 최대값이 존재하는 창구에 현재 사람을 넣는다. valid = False일때는 cycle이 k보다 작으면 새로운 창구에 curr을 넣어주고 cycle += 1을 한다. 만약에 이미 창구가 다 찬 상태면 False를 return 한다.
4. 마지막에 solution 함수가 return한 boolean값에 따라서 YES, 또는 NO를 출력한다.
```python
# Passport Control
# 그리디 알고리즘
import sys, math
input = sys.stdin.readline

N, k = map(int, input().split())
order = list(map(int, input().split()))
q = [0]*N
for idx, o in enumerate(order):
    q[o-1] = idx+1

stack = [[] for _ in range(k)]


start = q.pop(0)
stack[0].append(start)
def solution(q):
    cycle = 1
    while(q):
        curr = q.pop(0)
        valid = False
        temp = []
        for i in range(cycle):
            if curr > max(stack[i]):
                valid = True
                temp.append(i)
        if valid == False:
            if (cycle <= k-1):
                stack[cycle].append(curr)
                cycle += 1
            else:
                return False
        else:
            big = 0
            big_i = 0
            for i in temp:
                if big < max(stack[i]):
                    big = max(stack[i])
                    big_i = i
            stack[big_i].append(curr)

    return True

if solution(q):
    print('YES')
else:
    print('NO')
```


- Sol02
1. 주어지는 순서에 대해서 최소한의 필요로 하는 창구의 개수를 구해준다.
2. 만약에 필요로 하는 창구의 수가 현재 존재하는 창구의 수인 k보다 많으면 No를, 적거나 같으면 Yes를 출력하도록 한다.

#### 쿼드 압축 후 개수 세기
1. 결국에는 분할 정복 문제였다.
2. 그리고 실수 할 뻔 한 부분은 시작 index의 x좌표와 y좌표에 대해서 현재 정사각형의 한변 길이의 절반만큼 더해서 index의 첫 위치를 재귀적으로 구현해야 한다.
- 다른 사람들의 풀이도 나와 일치하는 것으로 보인다.
```python
import sys
input = sys.stdin.readline

N, k = map(int, input().split())
order = list(map(int, input().split()))
p = [[]for _ in range(N)]
for idx, o in enumerate(order):
    p[o-1] = idx+1
count = 0
stack = [0 for _ in range(N)]

for i in range(N):
    if (stack[i] == 0):
        count += 1
        big = p[i]

        for j in range(i+1, N):
            if (big < p[j] and stack[j] == 0):
                stack[j] = 1
                big = p[j]

if count > k:
    print('NO')
else:print('YES')
```
```python
# 쿼드압축 후 개수 세기
class Main():
    def square(self, start_x, start_y, n,arr):
        global answer
        if n == 1:
            if arr[start_y][start_x] == 0:
                answer[0] += 1
                return
            else:
                answer[1] += 1
                return
        else:
            first = arr[start_y][start_x]
            valid = True
            for x in range(start_x, start_x + n):
                for y in range(start_y, start_y + n):
                    if first != arr[y][x]:
                        valid = False
                        break
            if valid:
                if first == 0:
                    answer[0] += 1
                    return
                else:
                    answer[1] += 1
                    return
            else:
                dx, dy = [0,n//2,0,n//2],[0,0,n//2,n//2]
                for i in range(4):
                    self.square(start_x+dx[i], start_y+dy[i], n//2, arr)
        return
    def solution(self, arr):
        global answer
        n = len(arr)
        self.square(0,0,n,arr)
        return answer
```

