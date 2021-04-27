# Sol02 -> 이분 탐색 -> pypy3으로 제출해야만 시간 초과가 발생하지 않는다.
# 해결하고 보니 전형적인 이분탐색 문제였다.
# 만약에 valid하다면 더 긴 길이도 가능할 수도 있는 것이므려 left = mid + 1을 해 줄 조건이 성립
import sys
input = sys.stdin.readline

M, N = map(int, input().split())
arr = list(map(int, input().split()))
arr = sorted(arr, reverse = True)

answer = 0 
left, right = 1, max(arr)

def check(val):
    count = 0
    for i in range(N):
        count += arr[i]//val
    if count >= M:
        return True
    else:
        return False
answer = 0
while (left <= right):
    mid = (left + right) // 2
    if check(mid):
        answer = mid
        left = mid + 1
    else:
        right = mid - 1

print(answer)