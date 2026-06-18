1# Definition for a binary tree node.
2# class TreeNode(object):
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution(object):
8    def diameterOfBinaryTree(self, root):
9        """
10        :type root: Optional[TreeNode]
11        :rtype: int
12        """
13        self.res = 0
14
15        def dfs(node):
16            
17            if not node:
18                return 0
19            
20            left = dfs(node.left)
21            right = dfs(node.right)
22
23            self.res = max(self.res, left + right)
24
25            return 1 + max(left,right)
26        
27        dfs(root)
28        return self.res