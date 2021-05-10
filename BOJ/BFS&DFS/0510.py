# 10971
# dfs를 이용한 백트래킹으로 하면 pypy3만을 이용했을 때 정답 python3는 시간 초과
# 같은 dfs 함수를 이용하지만 중간중간 계속 answer과 값을 비교하면 시간초과 -> 260ms가 걸림
import sys, math
input = sys.stdin.readline

n = int(input())
cost = []
for _ in range(n):
    cost.append(list(map(int, input().split())))

def dfs(start, cur, check, price):
    global answer
    if sum(check) == n:
        if cost[cur][start] != 0:
            answer = min(answer, price+cost[cur][start])
        return
    for j in range(n):
        if (cost[cur][j] != 0 and check[j] == 0 and j != start):
            if price+cost[cur][j] < answer:
                check[j] = 1
                dfs(start, j, check, price + cost[cur][j])
                check[j] = 0

answer = math.inf
for i in range(n):
    check = [0]*n
    check[i] = 1
    dfs(i, i, check, 0)

print(answer)


