### 주제: BackTracking
#### BOJ 10971 외판원 순회2
첫 시도에는 pypy3으로만 통과가 되었다.   
일단 전형적인 백트래킹 문제 대로 bfs를 move()라는 함수를 이용해서 구현했으며, '길이 없을 수도 있다'라는 조건을 놓쳐서 그 부분을 확인하는 코드를 넣고  
출발지 제외 순회 완료 했음을 확인하는 부분에 오류가 있어서 그냥 sum(visit) == n일 때로 고쳤더니 답이 되었다.  
이제 python3로도 시간초과가 나지 않을 방법을 생각해 보아야 하는데, 일종의 greedy algorithm을 적용해서 재귀적으로 다음 단계를 불러오고자 할 때에 만약에 현재 ans보다 현재 추가되어서 나오는 비용이 더 크거나 작을 떄만 함수를 호출하도록 했다.  
그랬더니 2824ms에서 244ms로 줄고 python3로 통과가 되었다.
```py3
import sys
n = int(sys.stdin.readline())
board = []
for i in range(n):
    board.append(list(map(int, sys.stdin.readline().split())))


def move(start, temp, total):
    global visit, ans
    for i in range(n):
        if visit[i] == 0:
            if board[temp][i] != 0:
                if (total + board[temp][i]) <= ans:
                    visit[i] = 1
                    move(start, i, total + board[temp][i])
                    visit[i] = 0
    if sum(visit) == n:
        if board[temp][start] != 0:
            ans = min(ans, total+board[temp][start])

ans = 9999999999999
for i in range(n):
    visit = [0]*n
    visit[i] = 1
    move(i,i,0)
print(ans)
```

#### BOJ 2661번 좋은 수열
일단 좋은 수열을 판단하는 함수와 수열을 만들어주는 함수를 만들어서 수열을 오름차순으로 만들어 만약 valid한 수열이 있다고 하면 sys.exit()문으로 함수를 아얘 빠져 나가게 했다.  
그러나 수열을 만드는 과정에서 시간이 너무 오래 걸렸는지 python3와 pypy3모두 시간 초과가 발생했었다.  
알고리즘은 다 맞는 것 같아서 그냥 매번 함수를 재귀적으로 호출하기 전마다 valid한지 체크를 했는데 그 결과 시간초과가 없었다.  
```py3
import sys 
n = int(sys.stdin.readline())
def valid(strings):
    for i in range(1, len(strings)//2+1):
        for j in range(len(strings)-i):
            if strings[j:j+i] == strings[j+i:j+i*2]:
                return False
    return True


def make(made, v):
    if v == n-1:
        if valid(made):
            print(made)
            sys.exit()
        return
    for i in range(1, 4):
        if int(made[-1]) != i:
            if valid(made+str(i)):
                make(made+str(i), v+1)
    
make('1', 0)
```

#### 두 백트래킹 문제를 풀면서 얻은 결론은 재귀 함수는 호출할 수록 시간복잡도를 높인다는 점, 그렇기 때문에 중간 중간에 제한을 걸어서 **답이 될 수 없을 것들은 greedy의 관점으로** 중단해주는 것이 좋다.


#### BOJ 4132. Subset Sum
- 쉽게 풀 수 있는 백트래킹 문제였다. 우선 구하고자 하는 것은 주어진 값들을 이용해서 만들 수 있는, 한계값보다는 크거나 같지만 최소인 금액을 구하는 것이다. 중복 사용은 불가하니까 무조건 각각의 수를 순서대로 체크하면 된다.
- 시간 초과를 줄이기 위해서 다음 함수를 호출하기 전에 현재 값이 최소값보다 크면 재귀 함수를 부르지 않았다.
```py3
import sys
n,m = map(int, sys.stdin.readline().split())
milk = [int(sys.stdin.readline()) for _ in range(m)]
milk = sorted(milk)
made_milk = 99999999999
def make(temp, v):
    global made_milk
    if v == m:
        if temp == n:
            print(n)
            sys.exit()
        elif temp > n:
            made_milk = min(made_milk, temp)
        return
    else:
        if temp + milk[v] < made_milk:
            make(temp+milk[v], v+1)
        make(temp, v+1)

if sum(milk) < n:
    print('IMPOSSIBLE')
else:
    make(0,0)
    print(made_milk)
```


#### BOJ 1182. 부분 수열의 합
- n개의 정수로 이루어진 수열의 부분 수열의 합이 정해주는 수인 s일 때의 개수를 구하는 것이었다. 처음에는 시간 초과를 줄이기 위해서 먼저 주어진 n개의 수열을 정렬해서 s를 초과하면 바로 return 하려고 했으나, 알고 보니 '부분 수열'은 기존 수열의 순서와 일치 해야 하는 것이었기 때문에 정렬할 수는 없었다.
- 그러나 그 부분을 수정하고도 문제가 있었는데, s가 되었을 때 바로 return했기 때문이었다. 
- 이는 그렇게 해주면 수열게 양수, 음수, 0 모두 있기 때문에 다른 경우가 존재할 수 있기 때문이다. 따라서 그 부분을 수정해 주고, s일때에 원소가 포함되는 지의 여부까지 확인해주는 것을 추가하고 답이 맞았다.
```py3
import sys
n,s = map(int, sys.stdin.readline().split())
num = list(map(int, sys.stdin.readline().split()))
#부분 수열이면 원래 수열의 순서와 동일해야 하기 때문에 정렬해서 풀면 안됨
count = []
def find(temp, v, all):
    global count
    if temp == s and len(all):
        count.append(all)
    for i in range(v, n):
        find(temp + num[i], i+1, all+str(i))


find(0,0,'')
print(len(count))
```
