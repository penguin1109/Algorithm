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