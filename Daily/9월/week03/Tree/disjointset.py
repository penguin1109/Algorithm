# BOJ 20040 - 사이클 게임
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**8)

def find(node):
    if node == parent[node]:
        return node
    parent[node] = find(parent[node])
    return parent[node]

def check(a, b):
    a, b = find(a), find(b)
    if (a == b):
        return True
    else:
        return False
    
def union(a, b):
    a, b = find(a), find(b)
    if (a == b):
        return
    if (rank[a] > rank[b]):
        a, b = b, a
    parent[a] = b
    # 숫자가 더 큰 node를 무조건 parent가 되도록 한다.
    if (rank[a] == rank[b]):
        rank[b] += 1


n, m = map(int, input().split())
# 초기화 해주기
# 우선 각각의 node의 부모는 자기자신으로 설정
parent = [i for i in range(n)]
rank = [-1]*n
answer = 0
cycle = False
for _ in range(m):
    a, b = map(int, input().split())
    if cycle != True:
        # 연결해주려는 두 점이 같은 '집합'에 존재할 때에
        if check(a, b):
            cycle = True
            answer = _ + 1
        # 같은 '집합'이 아니라면 합쳐준다.
        else:
            union(a, b)

print(parent)
print(answer)