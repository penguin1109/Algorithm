import sys, math
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

N, K = map(int, input().split())
time = list(map(int, input().split()))

time.sort()
small = time[0]

ans = 0
num = N-1

while num >= 1:
    ans = max(ans, small * num + time[num] * (N-num))
    num -= 1

if K % ans:
    print(K//ans+1)
else:
    print(K//ans)