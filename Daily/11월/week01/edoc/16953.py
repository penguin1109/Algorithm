# 16953 - A -> B
# 정수 A를 B로 바꾸고자 할 때에 수행 가능한 연산이 2를 곱하거나 뒤에 1을 붙이는 것이 존재
# 최소 연산 수  + 1을 출력하시오

import sys
input = sys.stdin.readline

A, B = map(int, input().split())

from collections import deque
answer = 0
def BFS(num):
    global answer
    arr = deque([(str(num), 1)])
    while arr:
        temp, depth = arr.popleft()
        a, b = int(temp)*2, int(str(temp)+'1')
        if (a == B or b == B):
            answer = depth + 1
            return
        else:
            if (a < B):
                arr.append((a, depth+1))
            if (b < B):
                arr.append((b, depth+1))


BFS(A)
if answer == 0:
    print(-1)
else:
    print(answer)