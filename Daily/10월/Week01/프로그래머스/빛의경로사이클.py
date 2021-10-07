# 프로그래머스 - 빛의 경로 사이클
# 빛이 이동할 수 있는 경로 사이클의 개수와 각 사이클의 길이를 구하시오
grids = [["SL","LR"],["S"],["R","R"]]
from collections import deque

def cycle(x,y,dir,grid,check):
    # 가로 길이, 세로 길이
    n, m = len(grid[0]), len(grid)
    count = 1
    stack = deque()
    stack.append((x, y, dir))
    while stack:
        a,b,d = stack.popleft()
        count += 1
        a = a%n
        b = b%m
        if count >= (n*m)*(n*m):
            answer.append(count)
            return
        if check[b][a][d] != -1:
            continue
        else:
            check[b][a][d] = count
            
            if grid[b][a] == 'S':
                stack.append((b+dy[d], a+dx[d], d))
            elif grid[b][a] == 'R':
                new_dir = change_dir(d, 'R')
                stack.append((b+dy[new_dir], a+dx[new_dir], new_dir))
            elif grid[b][a] == 'L':
                new_dir = change_dir(d, 'L')
                stack.append((b+dy[new_dir], a+dx[new_dir], new_dir))

dx, dy = [1,0,-1,0], [0,1,0,-1]
def change_dir(dir, ch):
    if ch == 'S':
        return dir
    if ch == 'R':
        dir = dir + 1 if dir < 3 else 0
    else:
        dir = dir - 1 if dir > 0 else 3
    return dir
    


def solution(grid):
    global answer
    dx, dy = [1,0,-1,0], [0,1,0,-1]
    n, m = len(grid[0]), len(grid)
    check = [[[0 for _ in range(4)]for _ in range(n)]for _ in range(m)]
    for y in range(m):
        for x in range(n):
            for i in range(4):
                cur_dir, cur_x, cur_y = i, x, y
                if check[cur_y][cur_x][cur_dir] != 0:
                    continue
                step = 1
                while check[cur_y][cur_x][cur_dir] == 0:
                    check[cur_y][cur_x][cur_dir] = 1
                    step += 1
                    cur_x, cur_y = dx[cur_dir] + cur_x, cur_y + dy[cur_dir]
                    cur_x = cur_x % n
                    cur_y = cur_y % m

                    cur_dir = change_dir(cur_dir, grid[cur_y][cur_x])

                    
                answer.append(step-1)

    return answer

for g in grids:
    answer = []
    print(solution(g))