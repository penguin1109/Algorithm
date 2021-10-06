import sys
input = sys.stdin.readline
from collections import deque

# 처음부터 계속 틀렸디고 나왔었는데 아무리 봐도 정답인 것 같았다.
# 알고 보니 첫번째가 root node라는 보장이 없었기 때문이다.
N = int(input())
nodes = list(map(int, input().split()))
delete = int(input())

height = [0 for _ in range(N)]
tree = [[]for _ in range(N)]
group = []
root = 0
for idx, n in enumerate(nodes):
    if n != -1:
        tree[n].append(idx)
    else:
        root = idx
height[root] = 1
for idx, n in enumerate(nodes):
    if idx != root:
        height[idx] = height[n] + 1

q = deque([delete])
height[delete] = -1
group.append(q)
while q:
    temp = q.popleft()
    for n in tree[temp]:
        height[n] = -1
        group.append(n)
        q.append(n)

answer = 0
if height[root] != -1:
    q = deque([root])
    while q:
        temp = q.popleft()
        leaf = True
        for n in tree[temp]:
            if height[n] != -1:
                q.append(n)
                leaf = False
        if leaf == True:
            answer += 1

#print(group)
#print(height)
print(answer)