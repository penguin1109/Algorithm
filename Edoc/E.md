#### 1012 - 유기농 배추
#### 문제 설명
- 인접한 배추들을 그룹화해서 필요한 그룹의 최소 개수 구하기

#### 풀이 방법
1. 이동 방향을 상하좌우로 dx, dy배열에 저장
2. 1이 인접하지 않을 때까지 반복문과 deque를 이용해서 추가(1을 찾으면 0으로 변경)
3. 2중 for문을 사용해서 1이 등장하면 위의 2과정을 반복

#### 어려웠던 점
- 딱히 없음

#### 코드
1. 이지혜(python)
```py3
import sys
t = int(sys.stdin.readline())
from collections import deque
def count(board,x,y):
    global ans
    dx,dy = [-1,1,0,0],[0,0,-1,1]
    file = deque()
    file.append((x,y))
    while file:
        a,b = file.popleft()
        board[a][b] = 0
        for k in range(4):
            i,j = a+dx[k], b+dy[k]
            if 0<= i<n and 0<= j<m:
                if board[i][j] == 1:
                    board[i][j] = 0
                    file.append((i,j))
    ans += 1
    
for _ in range(t):
    m,n,k = map(int, sys.stdin.readline().split())
    board = [[0]*m for _ in range(n)]
    for _ in range(k):
        a,b = map(int, sys.stdin.readline().split())
        board[b][a] = 1
    ans = 0
    for x in range(m):
        for y in range(n):
            if board[y][x] == 1:
                count(board, y,x)
    print(ans)
```

2. 박지영(python)
```py3
import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    count = 0
    m, n, k = map(int, input().split())
    
    # 배추의 위치를 표시할 배열
    board = [[0]*(n+1) for _ in range(m+1)]
    # 배추 위치를 저장하는 배열
    arr = []
    
    for _ in range(k):
        x, y = map(int, input().split())
        board[x][y] = 1
        arr.append((x, y))
    
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    for i, j in arr:
        if not board[i][j]:
            continue
        count += 1
        # 탐색 진행할 배열
        stack = [(i, j)]
        while stack:
            x, y = stack[-1]
            stack.pop()
            for i in range(4):
                if board[x+dx[i]][y+dy[i]]:
                    board[x+dx[i]][y+dy[i]] = 0
                    stack.append((x+dx[i], y+dy[i]))

    print(count)
```
3. 배수아(C++)
```c++
#include<iostream>
#include<stack>
using namespace std;
typedef pair<int,int> ci;
stack <ci> s;
int mp[50][50];  //배추밭
int main()
{
   ci t;
   int dx[4]={-1,1,0,0}; //x 방향
   int dy[4]={0,0,-1,1}; //y 방향
   int tt,i,j,m,n,k,a,b,x,y,tx,ty,ans=0; 
   cin>>tt; //테스트케이스 개수
   while(tt--) 
   {
      cin>>m>>n>>k;
      for(i=0;i<k;i++)
      {
         cin>>a>>b;
         mp[b][a]=1; //배추 있는 곳
      }
      ans=0; //필요한 배추흰지렁이 개수
      for(i=0;i<n;i++) 
      {
         for(j=0;j<m;j++)
         {
            if(mp[i][j]==1)
            {
               ans++;
               mp[i][j]=0;
               s.push(ci(i,j));
               while(!s.empty()) //배추 확산되는 거 BFS로
               {
                  t=s.top();
                  s.pop();
                  x=t.first;
                  y=t.second;
                  for(k=0;k<4;k++)
                  {
                     tx=x+dx[k];
                     ty=y+dy[k];
                     if(tx>=0 && tx<n && ty>=0 && ty<m && mp[tx][ty]==1)
                     {
                        mp[tx][ty]=0;
                        s.push(ci(tx,ty));
                     }
                  }
               }
            }
         }
      }
      cout<<ans<<'\n';
   }   
   return 0;
}
```
