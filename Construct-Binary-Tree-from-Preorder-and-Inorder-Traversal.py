1# Definition for a binary tree node.
2# class TreeNode(object):
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution(object):
8    def buildTree(self, preorder, inorder):
9        """
10        :type preorder: List[int]
11        :type inorder: List[int]
12        :rtype: Optional[TreeNode]
13        """
14
15        if not preorder or not inorder:
16            return None
17        
18        root = TreeNode(preorder[0])
19        mid = inorder.index(preorder[0])
20
21        root.left = self.buildTree(preorder[1:mid+1], inorder[:mid])
22        root.right = self.buildTree(preorder[mid+1:], inorder[mid+1:])
23
24        return root
25        