t = int(input())
import math,heapq
def find(board):
    #key는 나중에 최소 가중치로 채울 것이기 때문에 가장 큰 값들로 채운다.
    key, visit, file = [9999999999999999999999]*n, [0]*n, []
    key[0] = 0
    heapq.heappush(file, (0,0))
    result = 0
    while file:
        #heapq가 최소 힙이기 떄문에 오름차순으로 가중치가 정렬된 상태로 저장이 된다.
        #가중치가 최소인 정점을 뽑는다.
        add, idx = heapq.heappop(file)
        #이미 방문한 적이 있다면 continue
        if visit[idx] == 1:
            continue
        #아니라면 노드 idx에서 이동할 수 있는, 아직 방문한 적이 없는 노드 찾기
        visit[idx] = 1
        result += add
        for i,j in board[idx]:
            #이어서 방문할 노드의 가중치가 현재까지 방문했던가중치보다 적어야 한다.
            if visit[i] == 0 and j < key[i]:
                #새로 갱신해 준다.
                key[i] = j
                heapq.heappush(file, (j,i))
    return result

for i in range(1, t+1):
    n = int(input())
    xlist = list(map(int, input().split()))
    ylist = list(map(int, input().split()))
    board = [[]for _ in range(n)]
    for k in range(n):
        for j in range(n):
            if k != j:
                x1,x2,y1,y2 = xlist[k],xlist[j],ylist[k],ylist[j]
                board[k].append((j,((x1-x2)**2+(y1-y2)**2)))
    e = float(input())
    result = find(board)
    print('#'+str(i)+' '+str(round(result*e)))
#파이썬 모듈중에 math.ceil()은 그냥 올림이고 round()가 반올림이다.


