1# Definition for a binary tree node.
2# class TreeNode(object):
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution(object):
8    def goodNodes(self, root):
9        """
10        :type root: TreeNode
11        :rtype: int
12        """
13
14        def dfs(root, maxi):
15            if not root:
16                return 0
17            res = 1 if root.val >= maxi else 0
18            maxi = max(maxi,root.val)
19
20            res += dfs(root.left,maxi)
21            res += dfs(root.right, maxi)
22
23            return res
24        
25        return dfs(root,root.val)
26        