1"""
2# Definition for a Node.
3class Node:
4    def __init__(self, x, next=None, random=None):
5        self.val = int(x)
6        self.next = next
7        self.random = random
8"""
9
10class Solution(object):
11    def copyRandomList(self, head):
12        """
13        :type head: Node
14        :rtype: Node
15        """
16
17        copylist = {None:None}
18        cur = head
19
20        while cur:
21            copy = Node(cur.val)
22            copylist[cur] = copy
23            cur = cur.next
24        
25        cur = head
26
27        while cur:
28            copy = copylist[cur]
29            copy.next = copylist[cur.next]
30            copy.random = copylist[cur.random]
31            cur = cur.next
32        
33        return copylist[head]