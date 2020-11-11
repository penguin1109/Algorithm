### 이진 검색 트리(Binary Search Tree)  
#### 이진 검색 트리의 조건  
1. 왼쪽 서브 트리의 노드의 key값은 자신의 노드의 key값보다 작아야 한다.
2. 오른쪽 서브 트리의 노드의 key값은 자신의 노드의 key값보다 커야 한다.

#### class Node구현  
```py3
class Node:
  def __init__(self, key, value):
    self.key = key
    self.value = value
    self.left = None
    self.right = None
```

- self.left와 self.right는 각각 왼쪽 자식 노드와 오른쪽 자식 노드에 대한 참조의 내용을 담고 있다.

#### class BinSearchTree 구현  
```py3
class BinSearchTree:
    def __init__(self):
        self.root = None
    def add(self, key, value):
        #_add_node함수는 node를 루트로 하는 sub tree에 키가 key이고 값이 value인 노드를 삽입한다.
        def _add_node(node, key, value):
            if key == node.key:
                return False
            elif key < node.key:
                if node.left is None:
                    node.left = Node(key, value)
                else:
                    _add_node(node.left, key, value)
            else:
                if node.right is None:
                    node.right = Node(key, value)
                else:
                    _add_node(node.right, key, value)
        #트리가 빈 상태이면 루트만으로 구성된 트리를 만들어야 하기 떄문에 루트만 있는 이진 검색 트리를 만든다.                    
        if self.root is None:
            self.root = Node(key, value)
            return True
        #트리가 비어있지 않기 떄문에 _add_node()함수를 호출하여 노드를 삽입한다.            
        else:
            return _add_node(self.root, key, value)
```        

```py3
class BinSearchTree:
    #처음에는 어떠한 노드도 참조하지 않기 때문에 빈 산태의 이진 검색 트리로 초기화 한다
    def __init__(self):
        self.root = None

    def add_node(self, value):
        self.root = self._add_node(self.root, value)
        return self.value is not None
    def _add_node(self, node, value):
        #해당 노드의 위치에 아무런 값도 존재하지 않는다면 노드의 데이터로 현재 노드를 대입
        if node is None:
            node = Node(value)
        #만약에 이미 트리에 존재하는 수이면 False를 return한다.
        elif value == node.value:
            return False
        else:
            if value < node.value:
                node.left = self._add_node(node.left, value)
            else:
                node.right = self._add_node(node.right, value)
        return node

    def search(self, key):
        return self._search(self.root, key)
    def _search(self, root, key):
        if root is None:
            return root is not None
        elif key < root.value:
            self._search(root.left, key)
        elif key > root.value:
            self._search(root.right, key)
        elif key == root.value:
            return root.value

    #삭제하는 경우는 3가지 경우로 나눌 수 있기 때문에 입력하는 경우보다 훨씬 복잡하다.
    #1. 자식 노드가 없는 노드를 삭제하는 경우
    #2. 자식 노드가 1개인 노드를 삭제하는 경우
    #3. 자식 노드가 2개인 노드를 삭제하는 경우
    def delete(self, key):
        p = self.root #현재 탐색중인 노드
        parent = None
        is_left_child = True    #p가 parent의 왼쪽 자식인지 확인
        #먼저 없애고자 하는 노드를 찾아야 한다.
        while True:
            if p is None:  #더이상의 진행이 불가능하면
                return False   #해당 키가 존재하지 않음을 의미
            if key == p.key:
                break
            else:
                parent = p
                if key < p.key:
                    is_left_child = True
                    p = p.left
                elif key > p.key:
                    is_left_child = False
                    p = p.right
        
        if p.left is None:  #p가 왼쪽 자식이 없다면
            if p is self.root:
                self.root = p.right
            elif is_left_child:   #p가 parent의 왼쪽 자식이라면 p가 이제 없기 때문에
                parent.left = p.right  #p의 오른쪽 자식이 parent의 왼쪽 자식이 된다. (오른쪽 자식이 있다면 그값이 저장될 것이고 없다면 None이 저장)
            elif not is_left_child:  #p가 parent의 오른쪽 자식이라면 
                parent.right = p.right   #p의 오른쪽 자식이 parent의 오른쪽 자식이 된다.
        
        elif p.right is None:  #p가 오른쪽 자식이 없다면
            if p is self.root:
                self.root = p.left
            elif is_left_child:
                parent.left = p.left
            elif not is_left_child:
                parent.right = p.left
        

        else:   #p가 오른쪽, 왼쪽 자식 모두 있다면
            parent = p
            left = p.left #p의 왼쪽 sub tree의 root
            is_left_child = True
            while left.right is not None:  #없애야 하는 노드의 왼쪽 subtree에서 제일 큰 수를 가진 node를 검색
                parent = left
                left = left.right
                is_left_child = False
            p.key = left.key
            p.value = left.value
            #만약에 제일 큰 노드가 자식이 없다면 그냥 삭제하면 되고
            #자식이 하나 존재하면 본인이 오른쪽 맨 끝 자식일 것이기 떄문에 더이상의 오른쪽자식이 존재할 수없고
            #따라서 left.left만 고려해 주면 된다.
            if is_left_child: #left가 parent의 왼쪽 자식이라는 뜻
                parent.left = left.left
            else:
                parent.right = left.left
```
#### 위에서 구현한 delete, 즉 원소 제거 함수에 대해 설명을 해보자면  
1. 삭제할 노드의 왼쪽 sub tree에서 제일 큰 노드를 찾는다.
2. 삭제할 노드의 위치의 key와 value값을 구해낸 제일 큰 노드의 값으로 바꾸어 준다.
3. 옮긴 노드를 삭제한다.
  3-1. 이떄에 옮긴 노드는 right child는 존재하지 않기 떄문에 자식이 1개(left)이거나 0개이다.
  3-2. 0개라면 그냥 없애주고
  3-3. 1개라면 해당 원소의 자식을 parent(제일 큰 노드의 parent)의 자식으로 
  
  
```py3
    def post_order(self):
        def _post_order(root):
            if root is None:  #비어있는 이진트리라면
                pass
            else:
                _post_order(root.left)
                _post_order(root.right)
                print(root.value)
        _post_order(self.root)
    
    def in_order(self):
        def _in_order(root):
            if root is None:   #비어있는 이진트리라면
                pass
            else:
                _in_order(root.left)
                print(root.value)
                _in_order(root.right)
        _in_order(self.root)
    
    def pre_order(self):
        def _pre_order(root):
            if root is None:    #비어있는 이진트리라면
                pass
            else:
                print(root.value)
                _pre_order(root.left)
                _pre_order(root.right)
        _pre_order(self.root)
```        
