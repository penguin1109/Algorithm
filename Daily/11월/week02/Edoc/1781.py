import sys, heapq
input = sys.stdin.readline

N = int(input())
max_t = 0
arr = []
for _ in range(N):
    a,b= map(int,input().split())
    arr.append((a, b))

arr = sorted(arr, key = lambda x: (x[0], x[1])) #데드라인과 컵라면의 개수를 모두 정렬한다.

def check(arr):
    h = []
    for i in arr:
        heapq.heappush(h, i[1])
        if (i[0] < len(h)):
            heapq.heappop(h)
    return sum(h)

    
ans = check(arr)
print(ans)

