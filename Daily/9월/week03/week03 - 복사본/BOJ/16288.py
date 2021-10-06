import sys
input = sys.stdin.readline

N, k = map(int, input().split())
order = list(map(int, input().split()))
p = [[]for _ in range(N)]
for idx, o in enumerate(order):
    p[o-1] = idx+1
count = 0
stack = [0 for _ in range(N)]

for i in range(N):
    if (stack[i] == 0):
        count += 1
        big = p[i]

        for j in range(i+1, N):
            if (big < p[j] and stack[j] == 0):
                stack[j] = 1
                big = p[j]

if count > k:
    print('NO')
else:print('YES')


