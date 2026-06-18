1# Definition for a binary tree node.
2# class TreeNode(object):
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution(object):
8    def isSubtree(self, root, subRoot):
9        """
10        :type root: Optional[TreeNode]
11        :type subRoot: Optional[TreeNode]
12        :rtype: bool
13        """
14        if not subRoot: return True
15        if not root: return False
16
17        if self.sameTree(root,subRoot): return True
18
19        return (self.isSubtree(root.left,subRoot) or self.isSubtree(root.right,subRoot))
20    
21    def sameTree(self,s,t):
22        if not s and not t:
23            return True
24        
25        if s and t and s.val == t.val:
26            return (self.sameTree(s.left,t.left) and self.sameTree(s.right,t.right))
27        
28        return False
29        