트리 알고리즘에 대해서 공부를 하던 와중에 '트리의 순회'라는 내용이 생소하게 와닿았다. 트리의 순회는 크게 전위 순회, 중위 순회, 그리고 후위 순회가 있다. 

전위 순회는 pre-order이라고 하는데, 왼쪽 노드 - 현재 노드 - 오른쪽 노드 의 순서로 트리를 순회한다. 

이 방법은 우선 현재 노드를 모두 순회한 뒤에 왼쪽과 오른쪽 서브 트리를 순회한다.   

BOJ 2263. 트리의 순회
이 문제는 결국에는 후위 순회와 중위 순회의 특징을 이용하여 재귀함수로 해결이 가능한 문제였다.

후위 순회의 경우에는 마지막 노드가 무조건 전체 트리 구조의 루트이다. 그리고 해당 루트 노드에 대해서 중위 순회에서 오른쪽에 위치한 노드들은 트리의 right sub-tree가, 왼쪽에 위치한 노드들은 트리의 left sub-tree가 된다. 



class Node:
    def __init__(self, value, left =[], right=[]):
        self.value = value
        self.left = left
        self.right = right


import sys, collections
input = sys.stdin.readline
n = int(input())
in_ = list(map(int, input().split()))
post_ = list(map(int, input().split()))

def in_order(node):
    if node is None:
        return
    in_order(node.left)
    print(node.value)
    in_order(node.right)

def post_order(node):
    if node is None:
        return
    post_order(node.left)
    post_order(node.right)
    print(node.value)

def pre_order(node):
    if node is None:
        return
    print(node.value, end = ' ')
    pre_order(node.left)
    pre_order(node.right)

tree = [0 for i in range(n+1)]

for i, j in enumerate(in_):
    tree[j] = i

def pre(i_s, i_e, p_s, p_e):
    if (i_s > i_e or p_s > p_e):
        return

    root = post_[p_e]
    print(root, end = ' ')

    root_idx = tree[root]

    left = root_idx - i_s
    right = i_e - root_idx

    pre(i_s, i_s + left - 1, p_s, p_s + left - 1)
    pre(i_e-right + 1, i_e, p_e-right, p_e-1) # post order에서는 마지막 노드 제외
    # in order에서는 root노드 제외 
    # in order에서 root 노드를 기준으로, 즉 현재 parent node를 기준으로 분할 정복을 이용해서 왼쪽 서브 트리와
    # 오른쪽 서브 트리를 구해준다.


pre(0, n-1, 0, n-1)
후위 순회에서 마지막에 나오는 부모 노드의 정보를 이용해서 중위 순회에서 왼쪽 자식 트리와 오른쪽 자식 트리로 분리 해 내는 것이 핵심이었다. 이진 탐색처럼 분할 정복을 이용해 중위 순회의 시작과 끝, 후위 순회의 시작과 끝의 index를 이용해서 재귀함수를 이용해서 전위 순회를 구현하면 된다. root, 즉 parent노드는 바로바로 출력해낸다.

주의해야 할 것은 sys.setrecursionlimit(10**8)을 이용해서 파이썬의 재귀 제한을 늘려주어야만 했다는 점이다.

그리고 트리 순회 문제를 해결할 때에 왼쪽 '노드'의 관점이 아니라 '서브 트리'의 관점으로 생각해야 쉽게 이해가 된다.


BOJ 7579. 앱
이 문제를 풀기 전에 간단한 사전 지식으로 dynamic programming의 유명한 베낭 문제가 있다. 애초에 동적 계획법으로 문제를 풀기 위해서는 분할 정복과 함께 공간 및 시간 복잡도를 줄이기 위해서 메모이제이션을 사용하여야 한다. 동적 계획법의 방법론을 이해해 주기 위해서 먼저 간단하게 피보나치 수 문제를 짚고 넘어가 보자 . 



예전에 풀려고 하다가 시간 초과 문제 때문에 실패 했던 문제이다. 