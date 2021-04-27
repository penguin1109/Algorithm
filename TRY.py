import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)
# 사이클이 있는 경우에 해당 사이클을 입력해서 저장하면 된다.
# 모든 사이클의 합을 구하면 된다.

N = int(input())
nums = []
for _ in range(N):
    nums.append(int(input()))

def dfs(start, node, res, check):
    """
    start -> int
    res -> str
    node -> int
    """
    if check[node-1] == 1: # 앞서 방문했었다면 return False
        return False
    if node == start: # 사이클을 이루면
        for i in res.strip(): # 지금까지 방문한 노드들에 대해서 check 배열에 확인
            check[int(i)-1] = 1
        return True
    if len(res) == N:
        return False
    if check[node-1] == 0:
        dfs(start, nums[node-1], res + str(node), check)


check = [0]*N
for i in range(1, N+1):
    if check[i-1] == 0:
        res = str(i)
        dfs(i, nums[i-1], res, check)

print(sum(check))
for i in range(len(check)):
    if check[i] == 1:
        print(i+1)
