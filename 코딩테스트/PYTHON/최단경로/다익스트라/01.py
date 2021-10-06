
# n개의 마을로 이루어진 나라
# k시간 이하로 배달이 가능한 마을에서만 주문을 받음
# 1번 마을을 시작으로 이동이 가능한 마을들의 개수를 반환하면 된다.
# 1번 마을로부터의 최단 거리를 구하는 다익스트라 알고리즘을 사용하면 된다.

def solution(N, road, K):
    answer = 0
    import math
    path = [0 for i in range(N)]
    # 가중치 저장
    weight = [[math.inf for i in range(N)]for i in range(N)]
    for i, val in enumerate(road):
        a, b, c = val[0]-1, val[1]-1, val[2]
        weight[a][b], weight[b][a] = min(weight[a][b], c), min(weight[b][a], c) 
        # 두 노드 사이의 경로의 가중치가 여러개 주어질 수도 있으므로 min값으로 저장
    def dijkstra(weigth):
        global N
        distance = weight[0]
        used = [0]
        distance[0] = 0
        while True:
            curr = used[-1]
            for i, val in enumerate(weight[curr]):
                if i not in used:
                    distance[i] = min(distance[i], distance[curr] + val)
            min_dist, idx = math.inf, 0
            for i, dist in enumerate(distance):
                if i not in used and dist < min_dist:
                    min_dist = dist
                    idx = i
            used.append(idx)
            if len(used) == N:
                break
        return distance
    distance = dijkstra(weight)
    for k in distance:
        if k <= K:
            answer += 1
    return answer


N, road, K = 6, [[1,2,1],[1,3,2],[2,3,2],[3,4,3],[3,5,2],[3,5,3],[5,6,1]], 4
print(solution(N, road, K))

        
        
        
            
            

# 743. Network Delay Time
import sys, collections, heapq
input = sys.stdin.readline

class Solution:
    def networkDelayTime(self,times, n, k):
        graph = collections.defaultdict(list)
        # 출발지, 도착지, 소요시간
        for u, v, w in times:
            graph[u].append((v, w))
        Q = [(0, k)]
        dist = collections.defaultdict(int)

        while Q:
            time, node = heapq.heappop(Q)
            if node not in dist:
                dist[node] = time
                for v, w in graph[node]:
                    temp = time + w
                    heapq.heappush(Q, (temp, v))
        
        if len(dist) == n:
            return max(dist.values())
        
        return -1


            



if __name__ == "__main__":
    times = [[2,1,1],[2,3,1],[3,4,1]]
    n,k = 4,2
    sol = Solution()
    answer = sol.networkDelayTime(times, n, k)
    print(answer)