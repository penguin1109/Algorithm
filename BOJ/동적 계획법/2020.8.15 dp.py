#2213 - 트리의 독립집합
#dp, dfs를 이용해서 재귀적으로 해결이 가능한 문제였다.
import sys
n = int(sys.stdin.readline())
cost = list(map(int, sys.stdin.readline().split()))
board = [[]for _ in range(n)]
for _ in range(n-1):
    v,e = map(int, sys.stdin.readline().split())
    board[v-1].append(e-1)
    board[e-1].append(v-1)
dp = [[0,0]for _ in range(n)]
#dp[i][0]은 i번 노드를 포함 했을 때의 최댓값, dp[i][1]은 i번 노드를 포함 안 했을 때의 최댓값
#올바른 답 출력을 위해서 노드의 경로를 저장해 주는 방법을 생각해 내는 것이 제일 힘들었다.
node = [[[],[]]for _ in range(n)]
check = [0]*n
#node[i][0]는 i번 노드 포함 했을 때 경로, node[i][1]는 i번 노드 포함 안 했을 때 경로
def dfs(v):
    check[v] = 1
    dp[v][0] += cost[v]
    node[v][0] += [v]
    for k in board[v]:
        if check[k] == 0:
            dfs(k)
            check[k] = 1
            dp[v][0] += dp[k][1]
            node[v][0] += node[k][1]
            if dp[k][0] < dp[k][1]:
                dp[v][1] += dp[k][1]
                node[v][1] += node[k][1]
            else:
                dp[v][1] += dp[k][0]
                node[v][1] += node[k][0]
dfs(0)
if dp[0][0] > dp[0][1]:
    print(dp[0][0])
    for k in node[0][0]:
        print(k+1,end = ' ')
else:
    print(dp[0][1])
    for k in node[0][1]:
        print(k+1,end = ' ')

#1937 - 욕심쟁이 판다
import sys
n = int(sys.stdin.readline())
board = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
#check 리스트를 굳이 따로 만들기보다는 애초에 dp에 저장하는 값을 0이 아닌 -1로 설정하여 혼동이 없도록 한다.
dp = [[-1]*n for _ in range(n)]
def dfs(x,y):
    dx,dy = [-1,1,0,0],[0,0,-1,1]
    res = 1
    for k in range(4):
        a,b = x+dx[k], y+dy[k]
        if 0<= a<n and 0<= b<n:
            if board[a][b] > board[x][y]:
                if dp[a][b] == -1:
                    #방문한 적이 없다면 재귀 호출을 통해 해당 노드에서의 최대 이동 거리를 불러옴(LIS)
                    res = max(res, dfs(a,b)+1)
                else:
                    res = max(res, dp[a][b]+1)
    dp[x][y] = res
    return res
for i in range(n):
    for j in range(n):
        #모든 노드를 방문할 때 까지
        if dp[i][j] == -1:
            dfs(i,j)
ans = 0
for k in range(n):
    ans = max(ans, max(dp[k]))
print(ans)

#1289 - 트리의 가중치
#재귀와 dp를 사용하는 문제인데, 사실 그것보다도 재귀의 기능을 더 많이 이용했다.
#일단 '모든 경로'의 가중치의 합을 구해야 했기 때문에
#visit리스트를 이용해서 방문했는지의 여부를 따져서 각 노드당 한번씩만 방문이 가능한 것이 절대 아니었다.
import sys
n = int(sys.stdin.readline())
sys.setrecursionlimit(10**7)
board = [[]for _ in range(n)]
for _ in range(n-1):
    a,b,c = map(int, sys.stdin.readline().split())
    board[a-1].append((b-1,c))
    board[b-1].append((a-1,c))
div= 1000000007 
ans = 0
def dfs(v,pre):
    global ans
    temp = 1
    for k in board[v]:
        idx, cost = k[0],k[1]
        if idx != pre:
            now = (cost*dfs(idx, v))%div
            ans = (ans + temp*now)%div
            temp = (temp+now)%div
    return temp
            
            
dfs(0,-1)
print(ans)
