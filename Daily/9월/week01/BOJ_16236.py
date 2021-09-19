# 백준 16236 - 아기 상어
# 자신의 크기와 같은 크기의 물고기를 먹어야 크기가 1만큼 증가
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)
N = int(input())
space = []
for _ in range(N):
    s = list(map(int, input().split()))
    if 9 in s:
        s_x, s_y = s.index(9), _
        s[s_x] = -1
    space.append(s)
dx, dy = [0,-1,1,0], [1,0,0,-1]
answer = []
def search(space, x, y, size, able):
    path = 0
    for i in range(4):
        x_, y_ = x + dx[i], y+dy[i]
        if ((0 <= x_ < N) and (0<= y_ < N)):
            if space[y_][x_] == 0:
                space[y_][x_] = -1
                search(space, x_, y_, size, able)
                space[y_][x_] = 0
            if space[y_][x_] < size:
                path += 1
                able.append((path, y_, x_))
                return
            elif space[y_][x_] == size:
                path += 1
                search(space, x_, y_, size, able)
        

def bfs(space,x,y, size, time, ate):
    able = []
    search(space, x, y, 2, able)
    if len(able) == 0:
        return time
    able = sorted(able)
    space[able[0][2]][able[0][1]] = -1
    if (ate + 1) == size:
        bfs(space, able[0][2], able[0][1], size+1, time+1, 0)
    else:
        bfs(space, able[0][2], able[0][1], size, time+1, ate+1)
    

print(bfs(space, s_x, s_y, 2, 0, 0))






