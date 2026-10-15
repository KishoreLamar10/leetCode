# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode | None) -> bool:
        self.Balanced = True

        def dfs(root):
            if self.Balanced == False or not root:
                return 0
            r = dfs(root.right)
            l = dfs(root.left)

            if abs(l - r) >  1:
                self.Balanced = False
            return 1 + max(l, r)
        
        dfs(root)
        return self.Balanced

            

        