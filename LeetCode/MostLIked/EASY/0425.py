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
            


#136. Single Number
# int형의 nums로 이루어진 배열에 대해서 하나의 수를 제외하고 모든 수가 두번씩 등장
# 두번 등장하는 하나의 수를 찾으시오

# Sol1
class Solution:
    def singleNumber(self, nums):
        """
        nums -> List[int]
        r -> int
        """
        if len(nums) == 1:
            return nums[0]
        else:
            nums.sort()
            start = nums.pop()
            while nums:
                if nums[-1] == start:
                    nums.pop()
                    start = nums.pop()
                else:
                    return start
        return start

# Sol2
from collections import defaultdict    
class Solution:
    def singleNumber(self, nums):
        hash_table = defaultdict(int)
        for i in nums:
            hash_table[i] += 1
        for j in hash_table:
            if hash_table[i] == 1:
                return i


# 283. Move Zeros
# two-pointer을 이용하면 쉽게 풀릴것으로 예상
# int형의 배열 nums가 주어질때 0이 아닌 수들의 순서는 유지하되 
# 0은 모두 배열의 끝에 옮김

# Sol1
class Solution:
    def moveZeroes(self, nums):
        non, zero = [], []
        for i in nums:
            if i == 0:
                zero.append(i)
            else:
                non.append(i)
        return non + zero
# Sol2    
class Solution:
    def moveZeroes(self, nums):
        a = len(nums)
        count = 0
        while a:
            curr = nums[0]
            nums.remove(curr)
            if curr == 0:
                count += 1
            else:
                nums.append(curr)
            a -= 1
        for _ in range(count):
            nums.append(0)
        return nums

# 763. Partition Labels
class Solution:
    def partitionLabels(self, s):
        """
        S -> str
        output -> List[int]
        """
        answer = []
        dict = {}
        for i in set(s.strip()):
            dict[i] = 0
        s = list(s.strip())
        for i in s:
            dict[i] += 1
        count = 0
        appear = set()
        idx = 0
        while idx < len(s):
            #print(appear)
            curr = s[idx]
            appear.add(curr)
            if dict[curr] - 1 == 0:
                appear.remove(curr)
            else:
                appear.add(curr)
            dict[curr] -= 1
            if not appear:
                appear = set()
                answer.append(count)
                count = 0
            else:
                count += 1
            idx += 1
        answer = list(map(lambda x: x+1, answer))
        return answer

# Sol2 - 같은 greedy로 해결한 풀이이지만 더 간결한 코드
class Solution:
    def partitionLabels(self, s):
        # 각 문자의 처음 등장하는 문자열의 index를 dictionary의 형태로 저장
        last = {c : i for i, c in enumerate(s)}
        ans = []
        j, anchor = 0, 0
        for i, c in enumerate(s):
            j = max(j, last[c])
            if i == j:
# 해당 문자가 새롭게 등장한 문자라면 그 이전까지의 지금까지의 문자열의 길이를 저장
                ans.append(i-anchor+1)
                anchor = i + 1

        return ans


# 70. Climbing Staris
# Sol1. 재귀적인 방법으로 해결 -> 시간 초과 발생
class Solution:
    def climb_Stairs(self, i, n):
        if (i > n):
            return 0
        if (i == n):
            return 1
        return self.climb_Stairs(i+1, n) + self.climb_Stairs(i+2, n)
    
    def climbStairs(self, n):
        return self.climb_Stairs(0, n)

# Sol2. Memoization 기법을 사용
# dynamic programming으로 해결할 수 있을 것
class Solution:
    def climbStairs(self, n):
        dp = [0]*n
        dp[0] = 1
        dp[1] = 2

        for i in range(2, n):
            dp[i] = dp[i-1]+dp[i-2]
        return dp[-1]