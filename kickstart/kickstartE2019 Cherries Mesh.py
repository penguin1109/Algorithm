#kick start Round E 2019
#Cherries Mesh
#n개의 노드, n-1개의 가중치, 최단거리 = MST알고리즘 이용
#가중치의 종류가 1,2로 두개밖에 없으므로 1로 최대한 조합을 만들고 나머지를 가중치2를 곱해더함
import sys
t = int(sys.stdin.readline())
def find(x):
    if board[x] < 0:
        return x
    board[x] = find(board[x])
    return board[x]

def merge(a,b):
    x,y = find(a), find(b)
    if x == y:
        return False
    board[y] = x
    board[x] = -1
    return True

for tc in range(1,t+1):
    n,m = map(int, sys.stdin.readline().split())
    board = [-1]*n
    ans, count = 0,0
    for i in range(m):
        a,b = map(int, sys.stdin.readline().split())
        if merge(a-1,b-1):
            ans += 1
    for j in range(n):
        if board[j] < 0:
            count += 1
    ans += (count-1)*2
    print('Case #%s: %s' %(str(tc), str(ans)))
