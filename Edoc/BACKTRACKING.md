#### 2231 - 분해합
```py3
import sys
sys.setrecursionlimit(10**8)

n = int(input())
answer = 1000001

def solution(k, check):
    print(list(str(k).strip()))
    print(check)
    global answer
    if k < 0:
        return
    elif check:
        if list(str(k).strip()) == check:
            answer = min(answer, k)
        else:
            for i in range(10):
                check.append(str(i))
                solution(k-i, check)
                check.remove(str(i))

    elif (check == []):
        for i in range(1, 10):
            check.append(str(i))
            solution(k-i, check)
            check.remove(str(i))

solution(n, [])

if answer == 1000001:
    print(0)
else:
    print(answer)
```

```py3
import sys
sys.setrecursionlimit(10**8)

input = sys.stdin.readline()
n = int(input)

ans = n+1

for i in range(n):
    file = [int(k) for k in str(i).strip()]
    if sum(file) + i == n:
        ans = min(ans, i)
        break

if ans == n+1:print(0)
else:print(ans)
```

#### 15649 - N과M(1)
```py3
import sys

n, m = map(int, sys.stdin.readline().split())
#1부터 n까지의 자연수 중에서 중복 없이 m개를 고른 수열
#수열은 사전 순으로 증가하는 순서로 출력해야 한다.

def solution(n, k, file):
    if k == m:
        for i in file:
            print(i, end = ' ')
        print()
    for i in range(1, n+1):
        if i not in file:
            file.append(i)
            solution(n, k+1, file)
            file.remove(i)

for i in range(1, n+1):
    solution(n, 1, [i])
```

#### 15650 - N과M(2)
```py3
import sys

n, m = map(int, sys.stdin.readline().split())
#1부터 n까지의 자연수 중에서 중복 없이 m개를 고른 수열
#수열은 오름차순이어야만 한다.

def solution(n, k, file):
    if k == m:
        for i in file:
            print(i, end = ' ')
        print()
    for i in range(file[-1]+1, n+1):
        if i not in file:
            file.append(i)
            solution(n, k+1, file)
            file.remove(i)

for i in range(1, n+1):
    solution(n, 1, [i])
```

#### 9382 - N과M(9) - EDOC
무조건
  1. 입력 받은 n개의 숫자가 담긴 리스트를 정렬한다.(오름차순으로)
  2. n개의 데이터에 대해서 해당 숫자를 사용 하였는지 안하였는지 check 리스트를 이용해서 확인해 주어야 한다.
- 파이썬에서 list데이터형에 append나 remove를 했을 때에 None을 return하게 되는데, 그걸 까먹고 계속 NoneType의 데이터를 재귀적으로 입력해서 문법적인 부분에 의한 오류가 한번 있었다.

```py3
import sys

n, m = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
#n개의 주어지는 자연수 중에서 중복 없이 m개를 고른 수열
#수열은 오름차순이어야만 한다.
answer = []

def solution(k, file, check):
    global answer, nums
    if k == m:
        if file not in answer:
            answer.append(file)
            for i in file:
               print(i, end = ' ')
            print()
    else:
        for i in range(n):
            if check[i] == False:
                check[i] = True
                temp = nums[i]
                new = file + [temp]
                solution(k+1, new, check)
                check[i] = False

check = [False] * n
nums.sort()
for i in range(n):
    temp = nums[i]
    check[i] = True
    solution(1, [temp], check)
    check[i] = False
```

- 위의 코드가 답이 나오기는 하는데 계속해서 answer 리스트에 현재 file이 있는지 없는지 확인하는 과정에서 시간 초과가 발생하였다.
- 따라서 아래와 같이 파이썬의 set는 중복을 허용하지 않는다는 특징을 이용해서 answer을 리스트 대신에 집합 자료형으로 변경해 주었더니 시간 초과를 해결할 수 있었다.

```py3
import sys

n, m = map(int, sys.stdin.readline().split())
nums = list(map(int, sys.stdin.readline().split()))
#n개의 주어지는 자연수 중에서 중복 없이 m개를 고른 수열
#수열은 오름차순이어야만 한다.
answer = set()

def solution(k, file, check):
    global nums, answer
    if k == m:
        if file not in answer:
            print(file)
            answer.add(file)
    elif k < m:
        for i in range(n):
            if check[i] == False:
                check[i] = True
                temp = nums[i]
                new = file + ' ' + str(temp)
                solution(k+1, new, check)
                check[i] = False

nums.sort()
for i in range(n):
    check = [False] * n
    check[i] = True
    temp = nums[i]
    solution(1, str(temp), check)
```

#### 1018 - 체스판 다시 칠하기
```py3
import sys

n,m = map(int, sys.stdin.readline().split())
color = []
for i in range(n):
    color.append(list(map(str, input().strip())))

answer = n*m
chess1, chess2 = [], []
for i in range(8):
    temp1,temp2 = [], []
    for j in range(8):
        idx = i*8+j
        if idx%2 == 0:
            temp1.append('W')
            temp2.append('B')
        else:
            temp1.append('B')
            temp2.append('W')
    if i % 2 == 0:
        chess1.append(temp1)
        chess2.append(temp2)
    else:
        chess1.append(temp2)
        chess2.append(temp1) 



def solution(x,y):
    global color, chess1, chess2
    ans = n*m
    new = []
    for i in range(8):
        new.append(color[x+i][y:y+8])
    count1, count2 = 0,0
    for i in range(8):
        for j in range(8):
            if new[i][j] != chess1[i][j]:
                count1 += 1
            if new[i][j] != chess2[i][j]:
                count2 += 1
    ans = min(count1, count2)
    return ans

for i in range(n-7):
    for j in range(m-7):
        answer = min(answer, solution(i,j))


print(answer)
```

#### 9663 - N-Queen
```py3
import sys

n = int(sys.stdin.readline())

answer = 0

def nQueen(k):
    global n, answer
    if k == n:
        answer += 1
        return

    for i in range(n):
        if check1[i] == -1:
            valid = True
            for m in range(k):
                if abs(i-check2[m]) == abs(m-k):
                    valid = False
                    continue
            if valid == True:
                check1[i] = 0
                check2[k] = i
                nQueen(k+1)
                check2[k] = -1
                check1[i] = -1


for i in range(n):
    check1,check2 = [-1]*n, [-1]*n   #check1은 세로, check2는 대각선
    #세로는 그 순번에 지정만 안하면 되는 것이고
    #대각선은 모든 위치가 일직선이 아니어야 하기 때문에 저장 위치가 중요
    check1[i] = 0
    check2[0] = i
    nQueen(1)

print(answer)
```

#### 2580 - 스도쿠 - EDOC
- 첫 시도에는 sudoku라는, 3x3크기의 정사각형 9개와 가로 방향의 스도쿠 조건 성립 여부를 확인하는 함수와 조합을 이용해서 세로의 가능한 경우들을 모두 (python의 itertool library의 combination 함수 사용) 구해서 새로운 스도쿠 조합을 만드는 make함수를 구현하였다.
  - 그러나 이렇게 하였더니 시간 초과가 발생해 버렸다. (아마 조합을 구하는 함수 때문일 수도 있다.)
- 그래서 방법을 바꾸고 백준의 백트래킹 알고리즘을 이용해 보라고 하길래 찾아보니 결국 내가 이해하고 있는 점과 유사하게, **DFS로 탐색하여 해결 상태에 도달하는 데 있어 불필요한 탐색을 하지 않는 것을 목표로**한다.
```py3
import sys
sys.setrecursionlimit(10**8)
import copy

data = []
for i in range(9):
    data.append(list(map(int, sys.stdin.readline().split())))

def sudoku(file):
    valid = True
    #3x3 정사각형
    for i in range(3):
        for j in range(3):
            x,y = i*3, j*3
            nums = [0]*10
            nums[0] = -1
            for k in range(x, x+3):
                for p in range(y, y+3):
                    if nums[file[k][p]] == 0:
                        nums[file[k][p]] = 1
                    else:
                        valid = False
                        return valid

    #가로
    for i in range(9):
        nums = [0]*10
        nums[0] = -1
        for j in range(9):
            if nums[file[j][i]] == 0:
                nums[file[j][i]] = 1
            else:
                valid = False
                return valid
    return valid

from itertools import permutations

def make(v, board):
    #세로 고려해서 만들기
    if v == 9:
        if sudoku(board):
            for i in range(9):
                for j in range(9):
                    print(board[i][j], end = ' ')
                print()
            sys.exit()
    else:
        nums = [int(i) for i in range(1, 10)]
        for i in range(9):
            if board[v][i] != 0:
                nums.remove(board[v][i])
        if nums:
            valid = list(permutations(nums, len(nums)))
            for example in valid:
                new = copy.deepcopy(board)
                index = 0
                for i in range(9):
                    if new[v][i] == 0:
                        new[v][i] = example[index]
                        index += 1
                make(v+1, new)

make(0, data)
```
- 시간 초과 난 것을 수정하기 위해 이전의 백트래킹 문제를 푼 것 처럼 그냥 check 리스트를 정사각형, 가로, 세로 확인 하는 것 별로 만들고 어차피 정사각형의 경우 시작점의 x, y좌표만 잘 확인하면 반복문을 이용해서 확인이 가능하기 때문에 재귀적으로 9x9, 즉 81번을 돌려주고
```py3
import sys
board = []
for _ in range(9):
    board.append(list(map(int, sys.stdin.readline().split())))

right = [[0]*9 for _ in range(9)]   #0이면 존재하지 않고 1이면 존재(가로 방향)
left = [[0]*9 for _ in range(9)]   #세로 방향
square = [[0]*9 for _ in range(9)]

for i in range(9):
    for j in range(9):
        if board[i][j] != 0:
            right[i][board[i][j]-1] = 1
            left[j][board[i][j]-1] = 1
            square[(i//3)*3+(j//3)][board[i][j]-1] = 1

def dfs(v):
    x,y = v//9, v%9
    if v == 81:
        for i in range(9):
            for j in range(9):
                print(board[i][j], end = ' ')
            print()
        sys.exit()
    if board[x][y] == 0:
        #i는 곧 해당 열/행/사각형에 모두 존재하지 않음이 확인될 경우 
        #(x,y)를 좌표로 갖는 0인 자리에 넣게 될 수의 후보군이다.
        for i in range(9):
            if right[x][i] == 0 and left[y][i] == 0 and square[(x//3)*3+(y//3)][i] == 0:
                #가로 방향의, 즉 x열에서 i라는 수가 존재하면 right[x][i] = 1
                #((x//3)*3, (y//3))의 좌표를 시작점으로 갖는 정사각형에 i라는 수가 존재하면 해당 값이 1
                right[x][i] = 1
                left[y][i] = 1
                square[(x//3)*3+(y//3)][i] = 1
                board[x][y] = i+1
                dfs(v+1)
                board[x][y] = 0
                right[x][i] = 0
                left[y][i] = 0
                square[(x//3)*3+(y//3)][i] = 0
    else:
        dfs(v+1)

dfs(0)
```

