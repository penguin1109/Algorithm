# 10844 - 쉬운 계단 수
# 인접한 모든 자리의 차이가 1인 수를 계단 수라고 한다.
# N이 주어질 때 길이가 N인 계단수가 총 몇개 있는지 구하여라

import sys
input = sys.stdin.readline
div = 1000000000
answer = 0
N = int(input()) # 1<= N <= 100

dp = [[0 for _ in range(10)] for _ in range(N)]
dp[0] = [1 for _ in range(10)]
dp[0][0] = 0

for i in range(1,N):
    if i == 0:
        continue
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][j+1]
        elif j == 9:
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]
answer = sum(dp[-1]) % div
print(answer)
