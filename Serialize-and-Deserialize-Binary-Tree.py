1# Definition for a binary tree node.
2# class TreeNode(object):
3#     def __init__(self, x):
4#         self.val = x
5#         self.left = None
6#         self.right = None
7
8class Codec:
9
10    def serialize(self, root):
11        """Encodes a tree to a single string.
12        
13        :type root: TreeNode
14        :rtype: str
15        """
16
17        res= []
18
19        def dfs(root):
20            if not root:
21                res.append("N")
22                return
23            res.append(str(root.val))
24            dfs(root.left)
25            dfs(root.right)
26        dfs(root)
27        return ",".join(res)
28        
29
30    def deserialize(self, data):
31        """Decodes your encoded data to tree.
32        
33        :type data: str
34        :rtype: TreeNode
35        """
36
37        val = data.split(",")
38        self.i = 0
39
40        def dfs():
41            if val[self.i] == "N":
42                self.i += 1
43                return None
44            
45            node = TreeNode(int(val[self.i]))
46            self.i += 1
47            node.left = dfs()
48            node.right = dfs()
49
50            return node
51        
52        return dfs()
53            
54        
55
56# Your Codec object will be instantiated and called as such:
57# ser = Codec()
58# deser = Codec()
59# ans = deser.deserialize(ser.serialize(root))