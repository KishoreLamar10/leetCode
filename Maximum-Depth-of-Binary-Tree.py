1# Definition for a binary tree node.
2# class TreeNode(object):
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution(object):
8    def maxDepth(self, root):
9        """
10        :type root: Optional[TreeNode]
11        :rtype: int
12        """
13
14        q = deque()
15
16        if root:
17            q.append(root)
18        
19        level = 0
20
21        while q:
22            for i in range(len(q)):
23                node = q.popleft()
24                if node.left:
25                    q.append(node.left)
26                if node.right:
27                    q.append(node.right)
28            level += 1
29        
30        return level
31        