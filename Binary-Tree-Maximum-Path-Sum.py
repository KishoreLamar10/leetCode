1# Definition for a binary tree node.
2# class TreeNode(object):
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution(object):
8    def maxPathSum(self, root):
9        """
10        :type root: Optional[TreeNode]
11        :rtype: int
12        """
13
14        res = [root.val]
15
16        def dfs(root):
17            if not root:
18                return 0
19            
20            left = dfs(root.left)
21            right = dfs(root.right)
22
23            leftM = max(left, 0)
24            rightM = max(right, 0)
25
26            res[0] = max(res[0], root.val + leftM + rightM)
27
28            return root.val + max(leftM, rightM)
29        
30        dfs(root)
31
32        return res[0]
33        