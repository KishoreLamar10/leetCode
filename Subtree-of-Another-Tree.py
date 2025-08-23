class Solution(object):
    def sameTree(self, a, b):
        if a is None and b is None:
            return True
        if a is None or b is None:
            return False
        if a.val != b.val:
            return False
        return self.sameTree(a.left, b.left) and self.sameTree(a.right, b.right)

    def isSubtree(self, root, subRoot):
        if subRoot is None:
            return True
        if root is None:
            return False
        if self.sameTree(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)
