import sys
input = sys.stdin.readline

n, x = map(int, input().split())
arr = list(map(int, input().split()))

ans = 0
arr.sort()

idx1 = 0
idx2 = n-1
while 0<=idx2<n and arr[idx2] == x:
    idx2 -= 1

ans += n - idx2 - 1

while idx1 < idx2:
    if arr[idx1]+arr[idx2] >= x/2:
        ans += 1
        idx1 += 1
        idx2 -= 1
    else:
        if idx1+2 <= idx2:
            idx1 += 3
            ans += 1
        else:
            break

print(ans)