import sys
input = sys.stdin.readline

n, m, k = map(int, input().split()) # n -> 배열의 크기 m -> 숫자가 더해지는 횟수 
# 주어진 수들을 m번 더해서 배열의 특정 index가 k번 이상 더해지지 않아서 만들 수 있는 제일 큰 수를 구하여라

nums = list(map(int, input().split()))

answer = 0
nums.sort(reverse = True)
fir, sec = nums[0], nums[1]

rep, more = m//(k+1), m%(k+1)

answer = (fir*k+sec) * rep + fir * more

print(answer)
