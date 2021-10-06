#### GREEDY
1. BOJ 2828 - 사과 담기 게임
```py
# 모든 사과를 담기 위한 바구니의 이동 거리의 최솟값을 구하여라
import sys
input = sys.stdin.readline



n, m = map(int, input().split())
j = int(input())

ans = 0
st, ed = 1, m

move = 0

for _ in range(j):
    place = int(input())
    if (place > ed): # 사과 위치 > 오른쪽 끝 
        move = (place - ed)
        st, ed = place - m + 1, place
    elif (place < st): # 사과 위치 < 왼쪽 끝
        move = (st - place)
        st, ed = place, place + m - 1
    else:
        move = 0
    ans += move

print(ans)
```
2. BOJ 1758 - 알바생 강호
```py
# 1758 - 알바생 강호
# 팁 = (강호에게 주려고 한 동 - 등수 - 1)
# 팁이 음수면 강호는 돈을 받을 수 없음
# 손님의 순서를 바꾸었을 때 받을 수 있는 팁의 최댓값은?

import sys
input = sys.stdin.readline

tips = []

N = int(input())
for _ in range(N):
    tips.append(int(input()))

tips = sorted(tips, reverse = True)
ans = 0
for order, tip in enumerate(tips):
    ans += max(0, (tip-order))

print(ans)
```

3. BOJ 4889 - 안정적인 문자열
- 문자열의 길이가 애초부터 짝수이기 때문에 아래와 같은 풀이가 가능하다.
- 그리디로 풀 수 있는 문제인 이유는 모든 경우의 수를 따지지 않고도 이미 {}와 같은 상태는 제외하고 나중에 한꺼번에 짝이 생성되지 않은 괄호끼리 묶어서 행할 수 있는 연산을 계산했기 때문이다.
 
```py
from collections import deque

def solution(string):
    change = 0
    stack = deque()
    string = deque(string)
    while string:
        curr = string.popleft()
        if not stack:
            stack.append(curr)
        else:
            if stack:
                if curr == '{':
                    stack.append(curr)
                else:
                    if stack[-1] == '{':
                        stack.pop()
                    else:
                        stack.append(curr)
    if stack:
        while stack:
            a, b = stack.popleft(), stack.popleft()
            # 두 괄호가 같으면 둘 중 하나만 바꿔주면 된다.
            if (a == b):
                change += 1
            # 두 괄호가 다르면서 순서가 바뀌어 있으면 두 괄호 모두 바꿔 주어야 한다.
            elif (a == '}' and b == '{'):
                change += 2


    return change

idx = 1
while True:
    ans = 0
    string = list(map(str, input().strip()))
    if '-' in string:
        break
    ans = solution(string)
    print(f'{idx}. {ans}')
    idx += 1
```

4. BOJ 1071 - 소트
```py
# 1071 - 소트
# n개의 정수가 주어질 때 연속된 두 수가 연속된 값이 아니게 정렬한다. ((i번째 수 + 1) =/= (i+1)번째 수)

import sys
input = sys.stdin.readline
def solution(nums):
    # 오름차순 정렬 (순서가 제일 낮은 것을 출력해야 하므로)
    nums = sorted(nums)
    group = []
    i = 0
    # 각각의 수와 개수를 배열로 저장
    while (i < len(nums)):
        curr = nums[i]
        count = 0
        for j in range(i, len(nums)):
            if (curr == nums[j]):
                count += 1
            else:
                break
        i += count
        group.append([curr, count])
    # index error이 발생할 수 있기 때문에 답에 영향을 주지 않는 값을 미리 넣어준다.
    # 0 이상의 정수로 이루어진 배열을 반환하는 것이기 때문에 -1보다 작은 값을 넣어야 함
    answer = [[-2,0]] 
    while group:
    # [숫자, 개수]를 저장한 리스트에 대해서 해당 리스트가 빈 배열이 될 때까지 진행
        if len(group) == 2 and group[0][0] + 1 == group[1][0]:
            answer.append([group[1][0],1])
            group[1][1] -= 1
            if group[1][1] == 0:
                group.pop(1)
        else:
        # else문에는 len(group) == 2인데 두 값이 연속이 아닌 경우도 포함 -> 이 때는 정답 배열의 마지막 수와 비교를 해야 함
            if (answer[-1][0] +1 != group[0][0]):
                answer.append([group[0][0], 1])
                group[0][1] -= 1
                if group[0][1] == 0:
                    group.pop(0)
            else:
                answer.append([group[1][0],1])
                group[1][1] -= 1
                if group[1][1] == 0:
                    group.pop(1)
    return answer

N = int(input())
nums = list(map(int, input().split()))
ans = solution(nums)

for i in ans:
    a,b = i[0], i[1]
    for _ in range(b):
        print(a, end = ' ')
```

