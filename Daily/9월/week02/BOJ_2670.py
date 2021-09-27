# dynamic programming
# 연속 부분 최대 곱
# 한 개 이상의 연속된 수들의 곱이 최대가 되는 부분을 찾아서 그 곱을 출력하시오
# 합이 아니라 곱이기 때문에 
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

N = int(input())
nums = [float(input()) for _ in range(N)]
dp = [-1] * N
dp[0] = nums[0]

def solution(n):
    if dp[n-1] == -1:
        dp[n-1] = max(nums[n-1], nums[n-1] * solution(n-1))
    return dp[n-1]

solution(N)
answer = max(dp)
print("%.3f" %answer)