import sys
input = sys.stdin.readline
from queue import PriorityQueue
que = PriorityQueue()

N, X = map(int, input().split())

C = sorted(list(map(int, input().split())))

ans = 0
for i in range(N):
    if C[i] == X:
        ans = N-i
        break
    elif C[i] < X:
        que.put(C[i])

while True:
    if que.qsize()  <= 1:
        break
    else:
        a, b = que.get(), que.get()
        temp = min(a+b+X/2, X)
        
    if temp == X:
        ans += 1
    elif temp < X:
        que.put(temp)

print(ans)
    

