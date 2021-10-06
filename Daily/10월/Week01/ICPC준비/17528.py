# 17528 - Two Machines
# 모든 작업을 완료하기 위해서 걸리는 시간의 최솟값을 구하여라

import sys
input = sys.stdin.readline
MAX = 250*250
n = int(input())
A, B = [], []
total = 0
for _ in range(n):
    a, b = map(int, input().split(' '))
    A.append(a)
    B.append(b)
    total += a


dp = [[MAX]*(total+1) for _ in range(n)]

dp[0][total] = 0
dp[0][total-A[0]] = B[0]
for i in range(n-1):
    for j in range(total+1):
        if (dp[i][j] != MAX):
            # i+1번째 작업을 B가 수행하지 않을 때
            dp[i+1][j] = dp[i][j]
            # i+1번째 작업을 B가 수행한다면 A는 i+1번째를 수행하지 않음
            dp[i+1][j-A[i+1]] = min(dp[i+1][j-A[i+1]], dp[i][j] + B[i+1])

answer = MAX
for i in range(total+1):
    answer = min(answer, max(i, dp[n-1][i]))

print(answer)
