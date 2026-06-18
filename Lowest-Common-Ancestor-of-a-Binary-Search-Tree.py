1# Definition for a binary tree node.
2# class TreeNode(object):
3#     def __init__(self, x):
4#         self.val = x
5#         self.left = None
6#         self.right = None
7
8class Solution(object):
9    def lowestCommonAncestor(self, root, p, q):
10        """
11        :type root: TreeNode
12        :type p: TreeNode
13        :type q: TreeNode
14        :rtype: TreeNode
15        """
16        cur = root
17
18        while cur:
19            if p.val > cur.val and q.val > cur.val:
20                cur = cur.right
21            elif p.val < cur.val and q.val < cur.val:
22                cur = cur.left
23            else:
24                return cur