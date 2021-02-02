## 02.03 스터디 - EDOC

#### 2504 - 괄호의 값
```py3
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
```py3
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
