import sys, heapq
input = sys.stdin.readline

N = int(input())
arr = []
for _ in range(N):
    arr.append(list(map(int, input().split())))

arr = sorted(arr, key = lambda x : (x[0], -x[1]))

q = []
for i in range(len(arr)):
    a,b = arr[i][0], arr[i][1]
    if (a > len(q)):
        heapq.heappush(q,b)
    else:
        comp = heapq.heappop(q)
        if (comp < b):
            heapq.heappush(q, b)
        else:heapq.heappush(q,comp)
print(sum(q))

        
