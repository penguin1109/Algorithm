import sys, math, heapq
input = sys.stdin.readline
INF = int(1e9)
def BelmanFord():
    visit = [INF for i in range(n)]
    visit[0] = 0

    for k in range(n): # 총 갱신을 원래는 n-1번 해주는 상황이지만
    # 음의 사이클을 감지하기 위해서 한 번 더 갱신을 해 준다.
    # 이때 k == n-1이라면 출발 노드로 돌아올 수 있다는 의미이기 때문에 'YES'를 출력한다.
        for i in range(n):
            for node in graph[i]:
                weight = graph[i][node]
                cost = visit[i] + weight
                if visit[node] > cost:
                    visit[node] = cost
                    if (k == n-1):
                        print('YES')
                        return
    print('NO')
    return
            
        
tc = int(input())
for _ in range(tc):
    n, m, w = map(int, input().split())
    graph = [{} for _ in range(n)]
    # 양방향 도로
    for _ in range(m):
        s, e, t = map(int, input().split())
        if (e-1 in graph[s-1].keys()):
            graph[s-1][e-1] = min(graph[s-1][e-1], t)
        else:
            graph[s-1][e-1] = t
        if (s-1 in graph[e-1].keys()):
            graph[e-1][s-1] = min(graph[e-1][s-1], t)
        else:
            graph[e-1][s-1] = t
    # 단방향 웜홀
    for _ in range(w):
        s, e, t = map(int, input().split())
        graph[s-1][e-1] = -t
    BelmanFord()



