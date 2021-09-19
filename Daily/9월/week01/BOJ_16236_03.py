import sys
input = sys.stdin.readline

from collections import deque
q = []

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
N = int(input())
data = [list(map(int, input().split())) for _ in range(N)]

fish = []
for i in range(N):
    for j in range(N):
        if data[i][j] != 0:
            if data[i][j] == 9:
                q.append((0, 2, i, j))
                data[i][j] = 0
            else:
                fish.append((data[i][j], i, j))

eat, result = 0, 0
while q:
    time, size, x, y = q.pop(0)
    test = []
    for i in range(len(fish)):
        if fish[i][0] < size:
            test.append((fish[i][1], fish[i][2]))
    if len(test) == 0:
        result = time
        break

    compare = []
    for a, b in test:
        temp = [[0]*N for _ in range(N)]
        s = []
        s.append((0, x, y))
        temp[x][y] = 1
        while s:
            c, aa, bb = s.pop(0)
            if aa == a and bb == b:
                compare.append((c, aa, bb))
                break
            for i in range(4):
                na, nb = aa+dx[i], bb+dy[i]
                if (0<=na<N and 0<=nb<N and data[na][nb] <= size):
                    temp[na][nb] = 1
                    s.append((c+1, na, nb))
    compare.sort()
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
    for f in fish:
        if f[1] ==  k[1] and f[2] == k[2]:
            fish.remove(f)
            break
print(result)
    

