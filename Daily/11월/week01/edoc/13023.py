import sys
input = sys.stdin.readline

n, m = map(int, input().split())
check = [0]*n
arr = [[] for i in range(n)]


for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    arr[a].append(b)
    arr[b].append(a)


def dfs(i, num):
    if num == 4:
        print(1)
        exit()
    for i in arr[i]:
        if not visited[i]:
            visited[i] = 1
            dfs(i, num + 1)
            visited[i] = 0

for i in range(n):
    visited[i] = 1
    dfs(i, 0)
    visited[i] = 0