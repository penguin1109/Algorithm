import sys, math
input = sys.stdin.readline
sys.setrecursionlimit(10**8)
inf = math.inf

N, M = map(int, input().split())
B_ = list(map(int, input().split())) # 메모리
C_ = list(map(int, input().split())) # 시간

dp = [0 for _ in range(sum(C_)+1)]

for i in range(N):
    cur_c, cur_b = C_[i], B_[i]
    for j in range(sum(C_), cur_c-1, -1):
        dp[j] = max(dp[j-cur_c]+cur_b, dp[j])


for i in range(sum(C_)+1):
    if dp[i] >= M:
        print(i)
        break