import sys
# 플로이드 와샬 알고리즘 (모든 정점 -> 모든 정점으로의 최단 경로) 
input = sys.stdin.readline


t = int(input())

def cost(ax,ay,bx,by):
    dx = abs(ax-bx)
    dy = abs(ay-by)
    return (dx+dy)


for _ in range(t):
    n = int(input())
    shop = []
    flag = [[0 for _ in range(n+2)] for _ in range(n+2)]
    for i in range(n+2):
        x,y = map(int, input().split())
        shop.append((x,y))
        flag[i][i] = 1
    
    for j in range(n+2):
        for k in range(n+2):
            ax,ay,bx,by = shop[j][0], shop[j][1], shop[k][0], shop[k][1]
            vc = cost(ax,ay,bx,by)
            if vc / 50 <= 20:
                flag[j][k] = flag[k][j] = 1

    for a in range(n+2):
        for b in range(n+2):
            for c in range(n+2):
                if flag[b][a] == 1 and flag[a][c] == 1:
                    flag[b][c] = 1
    
    if flag[0][n+1] == 1:
        print("happy")
    else:
        print("sad")


