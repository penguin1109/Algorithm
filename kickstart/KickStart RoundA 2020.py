#Kick Start Round A 2020
#Plates
import sys
t = int(sys.stdin.readline())
def maximize(file, p):
    dp = [[0]*(p+1) for _ in range(n+1)]
    for i in range(n):
        for j in range(1,k):
            file[i][j] = file[i][j] + file[i][j-1]
        file[i].append(0)
    for a in range(1,n+1):
        for b in range(1, p+1):
            for x in range(min(k, b)+1):
                dp[a][b] = max(dp[a][b], file[a-1][x-1]+dp[a-1][b-x])
    return dp


for i in range(t):
    n,k,p = map(int, sys.stdin.readline().split())
    file = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
    dp = maximize(file, p)
    res = 0
    for l in range(n+1):
        res = max(res, dp[l][-1])
    print('Case #%s: %s' %(str(i+1), str(res)))

#Workout
import sys
import math
t = int(sys.stdin.readline())
def minimize(sub,k):
    left, right = 1, max(sub)
    while left < right:
        mid = (left+right)//2
        if sum(map(lambda x: math.ceil(x/mid)-1, sub)) <= k:
            right = mid
        else:
            left = mid+1
    return left

for i in range(t):
    n,k = map(int, sys.stdin.readline().split())
    file = list(map(int, sys.stdin.readline().split()))
    sub = [file[i+1]-file[i] for i in range(len(file)-1)]
    res = minimize(sub, k)
    print('Case #%s: %s' %(str(i+1), str(res)))
