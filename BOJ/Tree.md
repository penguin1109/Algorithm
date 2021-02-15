#### 2606번 - 바이러스
```py
# 컴퓨터의 수와 네트워크상에 연결된 정보가 주어질 때에
# 1번 컴퓨터를 통해 바이러스에 걸리는 컴퓨터의 수를 출력하시오

import sys
from collections import deque
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

n = int(input()) # 컴퓨터의 수 (n<=100)
k = int(input()) # 네트워크에 연결된 컴퓨터의 쌍의 수
com = [[] for _ in range(n+1)] # 연결 리스트 만들기
# 양방향 연결 리스트
for _ in range(k):
    temp = list(map(int, input().split()))
    a, b = temp[0], temp[1]
    com[a].append(b)
    com[b].append(a)

answer = 0
check = [False]*(n+1)
check[1] = True
def dfs(idx):
    global answer, check
    if com[idx]:
        for i in range(len(com[idx])):
            temp = com[idx][i]
            if check[temp] == False:
                answer += 1
                check[temp] = True
                dfs(temp)
dfs(1)
print(answer)
```
#### 2263 - 트리의 순회
#### SOl1 - Tree Class 사용 (PyPy3, Python3 모두 시간초과/메모리 초과)
```py
# 2263번 - 트리의 순회
# n개의 정점을 갖는 이진 트리의 정점에 1부터 n까지의 번호가 중복 없이 매겨져 있음
# 첫째 줄에 프리오더를 출력한다.

import sys
sys.setrecursionlimit(10**8)
input = sys.stdin.readline

n = int(input())
In = list(map(int, input().split()))
Post = list(map(int, input().split()))

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    def __str__(self):
        return str(self.data)

class Tree:
    def __init__(self):
        self.root = None

    # 후위 순회        
    def postorder(self, node): 
        if node.left != None:
            self.postorder(node.left)
        if node.right != None:
            self.postorder(node.right)
        print(node, end = ' ')
    # 중위 순회
    def inorder(self, node):
        if node.left != None:
            self.preorder(node.left)
        print(node, end = ' ')
        if node.right != None:
            self.preorder(node.right)
    # 전위 순회
    def preorder(self, node):
        print(node, end = ' ')
        if node.left != None:
            self.inorder(node.left)
        if node.right != None:
            self.inorder(node.right)
    
    # 새로운 루트를 만들어 주어야 할 때에, 즉 새로운 트리를 만드는 경우에 root node를 생성해 주기 위해서 사용
    def makeRoot(self, node, left_node, right_node):
        if self.root == None:
            self.root = node
        node.left = left_node
        node.right = right_node
    
tree = Tree()
startIdx = (n-1)//2
num, level = n, 0
while (num):
    num -= 2**level
    level += 1
levels = [[]for _ in range(level)]

# 각각의 층별로 어떤 번호의 노드들이 존재하는지 입력해 넣기
# level을 키워나가면서 재귀적으로 왼쪽, 오른쪽에 있는 노드의 번호들을 각각의 입력에 넣어 준다.
def makeLevel(k, idx, level):
    if k == 1:
        levels[-1].append(idx+1)
        return
    else:
        levels[level].append(idx+1)
        temp = (k-1)//2
        makeLevel(temp, idx-temp, level+1)
        makeLevel(temp, idx+temp, level+1)
makeLevel(n, (n-1)//2, 0)

for i in range(1, len(levels)):
    if i == 1:
        root, left, right = Node(levels[i-1][0]), Node(levels[i][0]), Node(levels[i][1])
        tree.makeRoot(root, left, right)
    else:
        for j in range(2):
            root, left, right = Node(levels[i-1][j]), Node(levels[i][0+j*2]), Node(levels[i][1+j*2])
            tree.makeRoot(root, left, right)

tree.preorder(tree.root)
```
#### Sol2. Index사용(Python3 통과)
```py
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

n = int(input())
In = list(map(int, input().split()))
Post = list(map(int, input().split()))
# 포스트 오더에서 마지막에 있는 node가 전체 트리의 루트
#인오더에서 가운데(이는 완전 이진 트리이기 떄문에 가능) node가 전체 트리의 루트
Parent = [0 for _ in range(n+1)]
for i in range(len(In)): # 인덱스를 미리 저장해서 이후 Pre함수 실행시의 시간 단축
    node = In[i]
    Parent[node] = i

# 투 포인터 방법이 적용되어야만 시간초과/메모리 초과의 문제가 발생하지 않는다.
def Pre(In_start, In_end, Post_start, Post_end):
    if (Post_start <= Post_end):
        parent = Post[Post_end] 
        # Post Order은 각 서브 트리에서 루트 노드를 마지막으로 도달하기 때문에 Post Order리스트에서 각 서브 트리의 Parent노드를 찾는다.
        # 반면 Pre Order은 루트노드부터 위에서 차근차근 내려오며 탐색하는 방법이기 때문에 찾은 부모 노드를 출력하면 된다.
        print(parent, end = ' ')
        parent_index = Parent[parent]
        Left_left = parent_index - In_start # 왼쪽에 남은 노드의 수
        Right_left = In_end - parent_index # 오른쪽에 남은 노드의 수

        Pre(In_start, In_start+Left_left-1, Post_start, Post_start+Left_left-1) # 왼쪽 서브 트리 재귀 함수 실행
        Pre(In_end-Right_left+1, In_end, Post_end-Right_left, Post_end-1) # 오른쪽 서브 트리 재귀 함수 실행

Pre(0, n-1, 0, n-1) # 맨 처음과 맨 끝 index를 시작으로 함수를 실행
```

#### 1068 - 트리
```py
# BOJ 1068 - 트리
# 입력으로 주어진 노드를 지웠을 때에 리프 노드의 개수를 출력하여라

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

n = int(input()) # number of nodes
arr = list(map(int, input().split())) # 0번쨰부터 n-1번째 노드까지의 각 노드의 부모가 주어짐
k = int(input()) # 지울 노드의 번호

data = [[] for _ in range(n)]
for i in range(len(arr)):
    if arr[i] == -1:
        continue
    else:
        data[arr[i]].append(i) # data 배열에는 해당 index에 해당하는 노드의 자식이 리스트의 형태로 저장이 되어 있다.

valid = [True]*n
valid[k] = False
# 노드를 지우자
from collections import deque
answer = 0
for i in data:
    if not i:
        answer += 1 # 초기 leaf node의 개수

def delete(start):
    global answer
    arr = deque()
    arr.append(start)
    while arr:
        temp = arr.popleft()
        if data[temp]:
            for i in data[temp]:
                arr.append(i)
                valid[i] = False
        else:
            answer -= 1

delete(k)
# 예외 처리
# leaf node의 개수가 추가 될 수 있는 경우는 처음에 없애고자 하는 노드의 부모가 자식이 하나일때이다.
for i in range(len(data)):
    if k in data[i]: 
        if len(data[i]) == 1:
            answer += 1
print(answer)
```  

#### 11725 - 트리의 부모 찾기
- check 리스트를 사용하지 않고 answer리스트 만으로 해당 노드의 사용 여부를 확인했다는 점에서 큰 의의를 둔다.
```py
# 루트 없는 트리가 주어지고, 이때의 트리의 루트를 1이라고 정했을 때 각 노드의 부모를 구하시오

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8) # 그래프/트리 문제는 재귀의 깊이 설정이 필수

n = int(input()) # 노드의 개수 (2<=n<=100000)
data = [[] for _ in range(n+1)]
for _ in range(n-1):
    a, b = map(int, input().split())
    data[a].append(b)
    data[b].append(a)

answer = [-1]*(n+1) 

def sol(start):
    for node in data[start]:
        if answer[node] == -1:
            answer[node] = start
            sol(node)

sol(1)
if n == 2:
    print(1)
else:
    for i in range(2, n+1):
        print(answer[i])
```

#### 1967 - 트리의 지름
```py
# 1967 - 트리의 지름
# 트리의 지름이란 곧 가장 먼 두 정점 사이의 거리 혹은 가장 먼 두 정점을 연결하는 경로를 의마한다.
# 즉, 트리에 존재하는 모든 경로들 중에서 가장 긴 것의 길이를 의미한다.

import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

n = int(input()) # 노드의 개수 (1<=n<=10000)
nodes = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b,c = map(int, input().split())
    nodes[a].append((b,c)) # 각각의 index는 부모 노드의 번호이며, (자식 노드, 가중치)를 저장한다.
    nodes[b].append((a,c))

def maxDist(point, length):
    global answer, endPoint, visit
    if (visit[point] == True):
        return
    visit[point] = True
    if (answer < length):
        answer = length
        endPoint = point
    for i in range(len(nodes[point])):
        maxDist((nodes[point][i])[0], length + (nodes[point][i])[1])

answer = 0
visit = [False]*(n+1)
endPoint = 1
maxDist(1, 0)
visit = [False]*(n+1)
maxDist(endPoint, 0)

print(answer)
```