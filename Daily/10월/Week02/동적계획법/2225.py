# 2225 - 합분해
# 0부터 N까지의 정수 K개를 더해서 그 합이 N이 되는 경우의 수를 구하여라
# 덧셈의 순서가 바뀐 경우는 다른 경우로 세며, 한 개의 수를 여러번 쓸 수 있다.
div =  1000000000
import sys
input = sys.stdin.readline

N, K = map(int, input().split())
max_size = N*K+1
# dp[i][j]는 i개의 수를 사용할 때 합이 j인 경우의 수를 의미
# 중복 제거를 위해서 어떤 방법을 사용할지 -> 그냥 배열에 전부 넣거나 개수만 구하거나
dp = [[0 for _ in range(N+1)]for _ in range(K+1)]

for i in range(1, K+1):
    for j in range(N+1):
        if i == 1 and j <= N:
            dp[i][j] = 1
        elif i != 0:
            for k in range(j+1):
                dp[i][j] += dp[i-1][k]
print(dp[K][N]%div)
            
    
