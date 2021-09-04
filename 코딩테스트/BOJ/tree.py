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