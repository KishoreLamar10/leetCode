1# Definition for a binary tree node.
2# class TreeNode(object):
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution(object):
8    def isValidBST(self, root):
9        """
10        :type root: Optional[TreeNode]
11        :rtype: bool
12        """
13        def valid(node, left, right):
14            if not node:
15                return True
16            if not (left < node.val < right):
17                return False
18            
19            return valid(node.left, left, node.val) and valid(node.right,node.val,right)
20        
21        return valid(root,float('-inf'),float('inf'))
22        