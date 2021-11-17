# 9024 - 두 수의 합
import sys
input = sys.stdin.readline
from itertools import combinations
def solution(x, nums):
    '''두 수의 합이 K에 가깝도록 nums에서 두개의 수 선택'''
    mid = len(nums)//2
    l, r = mid, mid+1
    while (l >= 0 and r<= len(nums)-1):
        add = nums[l] + nums[r]
        if add == x:
            return True
        elif add < x:
            r += 1
        else:
            l -= 1
    return False

def answer(K, nums):
    m = max(abs(K-nums[-1]*2), abs(K-nums[0]*2))
    count = 0
    l, r = 0, len(nums)-1
    while (l < r):
        a, b = nums[l], nums[r]
        if (a+b == K):
            l += 1
            r -= 1
        elif (a+b > K):
            r -= 1
        else:
            l += 1
        if (abs(K-(a+b)) < m):
            m = abs(K-(a+b))
            count = 1
        elif (abs(K-(a+b)) == m):
            count += 1
    return count
def count(x, nums):
    answer = 0
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if (nums[i] + nums[i+1] > x or nums[i] + nums[-1] < x):
                break
            if nums[i] + nums[j] == x:
                answer += 1
            elif nums[i]+nums[j] > x:
                break
    return answer

t = int(input())

for _ in range(t):
    n, K = map(int, input().split())
    nums = list(map(int, input().split()))
    nums.sort() # 오름차순 정렬
    print(answer(K, nums))
           