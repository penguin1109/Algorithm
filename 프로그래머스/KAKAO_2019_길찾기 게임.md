### Kakao_2019_길 찾기 문제
- 일단 내가 정말 어려워 하는 트리 문제였다. 항상 문제를 제대로 이해하지 않으면 실수를 너무 많이 하기 때문에 우선 문제를 꼼꼼히 읽어 보았다.
- 문제는 사실 간단한 편에 속했다. 아무래도 자료구조 문제로 보였고, 따라서 새로운 트리를 만들고 전위 순회(preorder)와 후위 순회(post order)를 수행해야 하는 문제였는데 무조건 class Tree를 만들어서 객체관점에서봐야 할 것 같았다.
- 주어지는 nodeinfo 데이터는 각 노드의 x좌표와 y좌표였고, 각 루트 노드의 오른쪽 서브 트리의 노드들은 루트보다 x좌표가 크고 y좌표가 작으며, 왼쪽 서브 트리의 노드들은 x좌표와 y좌표가 모두 작아야 했다.
- 그래서 이 정보를 이용해서
  1. 주어진 nodeinfo에 index값을 추가하고 y좌표에 대해서 내림차순으로 정렬
  2. nodeinfo의 모든 node를 이용해 새로운 트리를 만듬
    1. root = None이면 새로운 노드에 의해 만든 newtree를 root로 설정
    2. root != None이면 현재 트리인 treenow에 root를 할당
    3. 이제 노드의 위치를 정해 주어야 하기 때문에 treenow.data[0] > newtree.data[0]일때 루트 노드가 x좌표가 더 큰 것이므로 newtree는 root의 왼쪽에 위치 해야 한다. 따라서 왼쪽 노드가 비었는지에 따라 자리가 결정된다.
      - treenow.left == None이면 treenow.left = newtree.data 이고 newtree.parent = treenow.data이고 break
      - treenow.left != None이면 treenow = treenow.left이다.
      **treenow.data[0] < newtree.data[0]일때도 마찬가지로, 이번엔 right로 진행해 준다.**
  3. 전위 순회, 후위 순회에 대해서 함수를 만들고 이를 answer list에 넣어주면 된다.
  - 전위 순회는 (노드 -> 왼쪽 자식 -> 오른쪽 자식)이기 때문에 자식 방문 전에 노드를 path에 넣음
  - 후위 순회는 (왼쪽 자식 -> 오른쪽 자식 -> 노드)이기 때문에 노드를 자식 방문 후에 path에 넣음
  
```py3
import sys
sys.setrecursionlimit(10**8)

class Tree:
    def __init__(self):
        self.parent = None
        self.left = None
        self.right = None
        self.data = None
        self.index = None

def preorder(root, path):
    if root == None:
        return path
    path.append(root.index)
    preorder(root.left, path)
    preorder(root.right, path)

    return path

def postorder(leaf, path):
    if leaf == None:
        return path

    postorder(leaf.left, path)
    postorder(leaf.right, path)
    path.append(leaf.index)
    return path
    

def solution(nodeinfo):
    root = None
    data, answer = [], []
    for idx, node in enumerate(nodeinfo):
        nodeinfo[idx].append(idx+1)
    data = sorted(nodeinfo, key = lambda x:x[1], reverse = True)  


    for idx, node in enumerate(data):
        newtree = Tree()
        newtree.index = node[2]
        newtree.data = node

        if root == None:
            root = newtree
        else:
            treenow = root
            while True:
                if newtree.data[0] > treenow.data[0]:

                    if treenow.right == None:
                        treenow.right = newtree
                        break
                    else:
                        treenow = treenow.right
                else:

                    if treenow.left == None:
                        treenow.left = newtree
                        break
                    else:
                        treenow = treenow.left
    answer.append(preorder(root, []))
    answer.append(postorder(root, []))

    return answer
```
