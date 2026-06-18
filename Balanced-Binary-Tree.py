1# Definition for a binary tree node.
2# class TreeNode(object):
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution(object):
8    def isBalanced(self, root):
9        """
10        :type root: Optional[TreeNode]
11        :rtype: bool
12        """
13        self.balanced = True
14
15        def dfs(root):
16            if self.balanced == False or not root:
17                return 0
18            
19            left = dfs(root.left)
20            right = dfs(root.right)
21
22            if abs(left - right) > 1:
23                self.balanced = False
24            
25            return 1 + max(left,right)
26        
27        dfs(root)
28        return self.balanced