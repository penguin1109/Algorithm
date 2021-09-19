import sys
input = sys.stdin.readline

from collections import deque
q = deque()

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]

fish = []

for i in range(N):
    for j in range(N):
        if data[i][j] != 0:
            if data[i][j] == 9:
                # time, size, x, y
                q.append((0, 2, i, j))
                data[i][j] = 0
            else:
                # 아기 상어를 제외한 다른 물고기 저장
                fish.append((data[i][j], i, j))

eat = 0
result = 0
while q:
    time, size, x, y = q.popleft()
    test = []
    for i in range(len(fish)):
        if size > fish[i][0]:
            test.append((fish[i][1], fish[i][2]))
    # 더이상 먹을 수 있는 물고기가 없다면 break
    if len(test) == 0:
        result = time
        break
    compare = []
    # 현재 위치로부터 먹을 수 있는 모든 물고기에 대해서 거리를 측정한다.
    for a,b in test:
        s = deque()
        temp = [[0]*N for _ in range(N)]
        temp[x][y] = 1
        s.append((0, x, y))
        while s:
            c, aa, bb = s.popleft()
            # 만약 현재 거리를 측정하려는 타겟 물고기에 도달하였다면
            if aa == a and bb == b:
                # 거리 비교를 위해서 compare배열에 저장
                compare.append((c, aa, bb))
                break
            # 도달할 수 없다면 사방으로 이동을 하여서 다시 s라는 큐에 넣어서 확인해 본다.
            for i in range(4):
                na, nb = aa + dx[i], bb + dy[i]
                if (0<=na<N and 0<=nb<N and data[na][nb] <= size and temp[na][nb] == 0):
                    temp[na][nb] = 1
                    s.append((c+1, na, nb))
    # 정렬해서 모든 물고기로 도달할 수 있는 거리를 구해준다.
    compare.sort()
    # 어떠한 물고기에도 도달할 수 없다면 break
    if len(compare) == 0:
        result = time
        break
    else:
        k = compare.pop(0)
    eat += 1
    if size == eat:
        size += 1
        eat = 0
    q.append((time+k[0], size, k[1], k[2]))
    for i in range(len(fish)):
        # 물고기중에서 방금 먹은 물고기는 없애준다.
        if fish[i][1] == k[1] and fish[i][2] == k[2]:
            fish.pop(i)
            break
print(result)
