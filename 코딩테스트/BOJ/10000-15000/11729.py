# 재귀 함수 - 하노이 탑 이동 순서
# 하노이탑 문제는 워낙 유명한 문제이다 보니 재귀로 풀어야 한다는 (문제를 더 작은 단위로 나누어야 한다는)
# 사실은 인지하고 있었으나 항상 관점을 결정하는 것이 제일 어려웠다
# hanoi 재귀 함수가 (n, start, to, via)로 정의가 되어 있다면
# n == 0일때 return 하고
# 나머지의 경우에는
# (n-1, start, via, to) 
# print(start, to)
# (n-1, via, to, start)
# 즉, n-1개의 탑을 start -> via로, n번째를 start -> to로, n-1개의 탑을 via -> to로 이동시키는 과정의 출력을 한다

import sys
input = sys.stdin.readline

n = int(input())

def hanoi(n, start, to, via):
    if n == 0:
        return
    else:
        hanoi(n-1, start, via, to)
        print(start, to)
        hanoi(n-1, via, to, start)

print(2**n-1)
hanoi(n, 1, 3, 2)





