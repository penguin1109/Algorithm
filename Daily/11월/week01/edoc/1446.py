# 최단경로 문제 (난이도 : 중)
import sys
input = sys.stdin.readline
# 도로를 역순으로 갈 수는 없음 
# 때문에 전체 이동해야 하는 길이인 D보다 도착지점이 더 크면 안됨(돌아갈 수가 없기 때문)
N,D = map(int, input().split())
dist = [0 for _ in range(D+1)]
# dist 배열에 해당 지점까지 이동하는데 움직여야 하는 거리를 저장
for d in range(D+1):
    dist[d] = d

route = dict()
for _ in range(N):
    start, end, length = map(int, input().split())
    if ((end <= D) and (length < end-start)):
        if start not in route:
            route[start] = []
        route[start].append((end, length))

before = -1
for i in range(D+1):
    if (i != 0):
        before = dist[i-1]
    dist[i] = min(dist[i], before+1)
    if (i in route):
        for r in route[i]:
            end, length = r[0], r[1]
            if (dist[i] + length < dist[end]):
                dist[end] = dist[i]+ length
            
print(dist[D])
