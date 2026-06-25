1# Definition for a binary tree node.
2# class TreeNode(object):
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution(object):
8    def minDepth(self, root):
9        """
10        :type root: Optional[TreeNode]
11        :rtype: int
12        """
13        if not root:
14            return 0
15
16        q = deque([root])
17        
18        depth = 1
19        while q:
20            qLen = len(q)
21            for i in range(qLen):
22                node = q.popleft()
23                if not node.left and not node.right:
24                    return depth
25                if node.left:
26                    q.append(node.left)
27                if node.right:
28                    q.append(node.right)
29            
30            depth += 1
31        
32
33
34        