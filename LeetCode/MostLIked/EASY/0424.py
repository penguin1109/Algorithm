# 617. Merge Two Binary Trees
class TreeNode:
    """
    TreeNode class를 살펴 보면 val, left, right의 변수를 입력받아야 하며
    문제의 Solution의 입력값으로 주어지는 root1, root2배열들의 각각의 요소들은 모두 TreeNode이다
    따라서 우리는 단순히 배열로 볼 것이 아니라 마지막에 답을 반환할 때에도
    TreeNode의 배열을 반환해야 한다.

    하나의 TreeNode를 생성하는 방법은
    t = TreeNode(원하는 root Node의 값)
    t.left = left node값
    t.right = right node값
    """
    
    def __init__(self, val = 0, left = None, right = None):
        self.value = val
        self.left = left
        self.right = right
# Sol1. 재귀적으로 해결하는 경우
class Solution01:
    def mergeTrees(self, root1, root2):
        """
        root1 -> TreeNode
        root2 -> TreeNode
        """
        if not root1:
            return root2
        if not root2:
            return root1
        root1.val += root2.val
        root1.left = self.mergeTrees(root1.left, root2.left)
        root1.right = self.mergeTrees(root1.right, root2.right)

# Sol2. 
class Solution02:
    def mergeTrees(self, root1, root2):
        stack = []
        # 둘 중 하나라도 노드가 NULL값이면 다른 노드를 반환한다.
        if not root1:
            return root2
        if not root2:
            return root1
        
        t = TreeNode(0)
        t.left = TreeNode(1)
        t.right = TreeNode(1)

        stack.append(root1)
        stack.append(root2)
        stack.append(t)

        while stack:
            node_0, node_1, node_2 = stack.pop(), stack.pop(), stack.pop()
            if node_0 and node_1 and node_2:
                node_0.val = node_1.val + node_2.val
                
                if not node_1.left:
                    node_0.left = node_2.left
                elif not node_2.left:
                    node_0.left = node_1.left
                else: # 둘 다 존재하는 경우
                    stack.append(node_1.left)
                    stack.append(node_2.left)
                    if not node_0.left:
                        node_0.left = TreeNode(0)
                    stack.append(node_0.left)
                
                if not node_1.right:
                    node_0.right = node_2.right
                elif not node_2.right:
                    node_0.right = node_1.right
                else: # 둘 다 존재하는 경우
                    stack.append(node_1.right)
                    stack.append(node_2.right)
                    if not node_0.right:
                        node_0.right = TreeNode(0)
                    stack.append(node_0.right)

        return t
            


