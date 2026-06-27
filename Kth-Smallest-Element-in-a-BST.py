1# Definition for a binary tree node.
2# class TreeNode(object):
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution(object):
8    def kthSmallest(self, root, k):
9        """
10        :type root: Optional[TreeNode]
11        :type k: int
12        :rtype: int
13        """
14
15        arr = []
16
17        def dfs(node):
18            if not node:
19                return
20            
21            dfs(node.left)
22            arr.append(node.val)
23            dfs(node.right)
24
25        dfs(root)
26        return arr[k-1]        