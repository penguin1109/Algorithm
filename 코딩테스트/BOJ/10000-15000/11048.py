# 동적 계획법
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)
n, m = map(int, input().split())
dx,dy = [1,0,1], [0,1,1]

candy = []
for _ in range(n):
    candy.append(list(map(int, input().split())))

check = [[-1]*m for _ in range(n)]
check[0][0] = candy[0][0]
answer = 0

for i in range(n):
    for j in range(m):
        if i == 0 and j == 0:
            check[i][j] = candy[0][0]
        elif i == 0:
            check[i][j] = candy[i][j] + check[i][j-1]
        elif j == 0:
            check[i][j] = candy[i][j] + check[i-1][j]
        else:
            check[i][j] = candy[i][j] + max(check[i-1][j], check[i][j-1], check[i-1][j-1])
def move(a, b):
    global answer
    if a == m and b == n:
        return
    elif a > m or b > n:
        return
    else:
        for k in range(3):
            x = a + dx[k]
            y = b + dy[k]
            if x <= m and y <= n:
                if check[y-1][x-1] == -1:
                    check[y-1][x-1] = check[b-1][a-1] + candy[y-1][x-1]
                else:
                    check[y-1][x-1] = max(check[y-1][x-1], check[b-1][a-1] + candy[y-1][x-1])
                move(x, y)

#move(1, 1)
print(check[n-1][m-1])
            