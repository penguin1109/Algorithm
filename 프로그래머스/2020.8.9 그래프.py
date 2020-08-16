#2020.8.9 그래프 알고리즘

#가장 먼 노드(프로그래머스)
#처음에는 visited 리스트를 비트 마스킹으로 갱신해야 cycle형태의 연결 형태를 주의할 수 있을것이라
#생각했었으나 그게 아니라 매번 연결된 노드에 대해 deque와 1차원 visited리스트 하나만 있으면 되었다.
def move(now, visited,board,dp):
    if len(board[now]) > 0:
        for k in board[now]:
            if visited & (1<<k) == 0:
                dp[k] = min(dp[k], dp[now]+1)
                move(k, visited|(1<<k),board,dp)
def solution(n, edge):
    inf = float('inf')
    dp = [inf]*n
    board = [[]for _ in range(n)]
    for i in range(len(edge)):
        a,b = edge[i][0]-1, edge[i][1]-1
        board[a].append(b)
        board[b].append(a)
    dp[0] = 0
    move(0, 1<<0,board,dp)
    ans = 0
    for i in dp:
        if i == max(dp):
            ans += 1
    return ans


#순위(프로그래머스)
#이 문제는 선수를 노드, 경기를 간선으로 취급하여 board에 선수들, 즉 노드들 끼리의 이김,짐,불확실 여부를
#1,-1,0으로 갱신하였다.그리고 만약에 board[i][j] == board[j][k]이면
#board[i][k]를 같은 값으로 갱신했다.
#다만 반대의 경우도 반대 부호를 가진 값으로 갱신해 주어야 했었기에 그것을 놓치는 바람에 다시 풀었다.
#일종의 그래프와 Floyd-Marshal알고리즘을 이용해 해결해야 했던 그래프 문제였다.

def move(now, visited,board,dp):
    if len(board[now]) > 0:
        for k in board[now]:
            if visited & (1<<k) == 0:
                dp[k] = min(dp[k], dp[now]+1)
                move(k, visited|(1<<k),board,dp)
def solution(n, edge):
    inf = float('inf')
    dp = [inf]*n
    board = [[]for _ in range(n)]
    for i in range(len(edge)):
        a,b = edge[i][0]-1, edge[i][1]-1
        board[a].append(b)
        board[b].append(a)
    dp[0] = 0
    move(0, 1<<0,board,dp)
    ans = 0
    for i in dp:
        if i == max(dp):
            ans += 1
    return ans
    
