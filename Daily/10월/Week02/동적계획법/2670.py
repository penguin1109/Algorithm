# 2670 - 연속 부분 최대 곱
# 계산된 최댓값을 소수점 이하 넷째 자리에서 반올림하여 소수점 이하 셋째 자리까지 출력
import sys
input = sys.stdin.readline

# 이런 문제 풀 때 제일 먼저 고려할 것은 순서대로 입력과 동시에 처리할지 아니면 입력을 모두 받고 처리할지


N = int(input())  # N은 10000이하의 자연수
nums = list(map(float, [input().strip() for _ in range(N)]))

#dp[i]는 i번째 수를 곱할 때 제일 큰 값
dp = [-1 for _ in range(N)]
dp[0] = nums[0] 

def rec(n):
    if dp[n-1] == -1:
        dp[n-1] = max(rec(n-1)*nums[n-1], nums[n-1])
    return dp[n-1]

rec(N)
print("%0.3f" %max(dp))