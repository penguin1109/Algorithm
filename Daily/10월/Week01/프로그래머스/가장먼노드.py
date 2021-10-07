# 프로그래머스 - 가장 먼 노드
import sys
input = sys.stdin.readline
from collections import deque


def dfs(node,arr):
    global answer
    n = len(arr)
    stack = deque()
    check = [False for _ in range(n+1)]
    check[node] = True
    count = 0
    stack.append((node, 0))
    while stack:
        curr_node, curr_count = stack.popleft()
        for n in arr[curr_node]:
            if check[n] == True:continue
            check[n] = True
            answer[n] = curr_count+1
            stack.append((n, curr_count+1))
        

def solution(n, vertex):
    result = 0
    arr = [[] for _ in range(n+1)]
    for v in vertex:
        a,b = v[0], v[1]
        arr[a].append(b)
        arr[b].append(a)
    dfs(1, arr)
    big = max(answer)
    for a in answer:
        if a == big:result +=1
    return result

n, vertex = 6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
answer = [0 for _ in range(n+1)]
print(solution(n, vertex))