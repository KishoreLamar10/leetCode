1# Definition for a binary tree node.
2# class TreeNode(object):
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution(object):
8    def invertTree(self, root):
9        """
10        :type root: Optional[TreeNode]
11        :rtype: Optional[TreeNode]
12        """
13
14        if not root:
15            return None
16
17        temp = root.left
18        root.left = root.right
19        root.right = temp
20
21        self.invertTree(root.left)
22        self.invertTree(root.right)
23
24        return root
25        