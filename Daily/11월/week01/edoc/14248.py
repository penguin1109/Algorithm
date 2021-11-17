# Dfs, Bfs 문제 - 점프점프
import sys
input = sys.stdin.readline

n = int(input())
dist = list(map(int, input().split()))
s = int(input()) # 시작 지점

flag = [0 for _ in range(n+1)]
flag[0] = 1
answer = 1
# 영우가 방문 가능한 돌들의 개수를 구하시오
def dfs(node):
    global answer
    shift = dist[node-1];
    l, r = node-shift, node+shift
    if (l >= 1 and flag[l] == 0):
        flag[l] = 1
        answer += 1
        dfs(l)
    if (r <= n and flag[r] == 0):
        flag[r] = 1
        answer += 1
        dfs(r)

dfs(s)
print(answer)