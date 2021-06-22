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


# 16234 - 인구 이동
import copy, sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

n, l, r = map(int, input().split())
A = []
for _ in range(n):
    A.append(list(map(int, input().split())))

answer = 0

def check(a,b):
    if l <= abs(a-b) <= r:
        return True
    else:
        return False
    
def dfs(x, y):
    global group, group_count_sum
    graph_group[x][y] = group # 어떤 group인지 저장
    group_count_sum[group][0] += 1 # 해당 group의 나라 개수 더하기
    group_count_sum[group][1] += A[x][y] # 인구수 더하기
    
    dx, dy = [-1, 0, 1, 0], [0, -1, 0, 1]
    for i in range(4):
        X, Y = x+dx[i], y+dy[i]
        if 0<=X<n and 0<=Y<n:
            if graph_group[X][Y] == 0 and check(A[x][y], A[X][Y]):
                graph_group[X][Y] = group
                dfs(X, Y)
                
# 더이상의 인구 변화가 없으면 True를 반환
def is_same(graph, graph_raw):
    for i in range(n):
        for j in range(n):
            if graph[i][j] != graph_raw[i][j]:
                return False
    return True

while True:
    group = 0
    graph_group = [[0]*n for _ in range(n)]
    group_count_sum = [[0]*2 for _ in range(n**2)] # 최대 n개의 그룹까지밖에 못 만들어짐
    graph_raw = copy.deepcopy(A)
    for i in range(n):
        for j in range(n):
            if graph_group[i][j] == 0:
                dfs(i, j)
                group += 1
    for i in range(n):
        for j in range(n):
            g = graph_group[i][j]
            A[i][j] = group_count_sum[g][1] // group_count_sum[g][0]
    if is_same(A, graph_raw):
        break
    else:
        answer += 1

print(answer)

# 1. dfs를 이용해서 같은 국경으로 취급이 가능하면 묶어줌
# 2. 같은 국경이면 이동을 시켜줌
# 3. 위의 1, 2를 반복해서 변화가 없으면 멈춤
# 아무리 해도 메모리 초과가 발생




