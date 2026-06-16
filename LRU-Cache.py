1class Node:
2    def __init__(self,key,val):
3        self.key = key
4        self.val = val
5        self.next, self.prev = None, None
6
7class LRUCache(object):
8
9    def __init__(self, capacity):
10        """
11        :type capacity: int
12        """
13
14        self.capacity = capacity
15        self.cache = {}
16
17        self.left,self.right = Node(0,0), Node(0,0)
18        self.left.next, self.right.prev = self.right, self.left
19    
20    def remove(self,node):
21        prev, nxt = node.prev, node.next
22        prev.next = nxt
23        nxt.prev = prev
24    
25    def insert(self,node):
26        prev,nxt = self.right.prev, self.right
27        prev.next = nxt.prev = node
28        node.next, node.prev = nxt, prev
29
30    def get(self, key):
31        """
32        :type key: int
33        :rtype: int
34        """
35        if key in self.cache:
36            self.remove(self.cache[key])
37            self.insert(self.cache[key])
38            return self.cache[key].val
39        
40        return -1
41        
42
43    def put(self, key, value):
44        """
45        :type key: int
46        :type value: int
47        :rtype: None
48        """
49
50        if key in self.cache:
51            self.remove(self.cache[key])
52
53        self.cache[key] = Node(key,value)
54        self.insert(self.cache[key])
55        
56        if len(self.cache) > self.capacity:
57            lru = self.left.next
58            self.remove(lru)
59            del self.cache[lru.key]
60        
61
62
63# Your LRUCache object will be instantiated and called as such:
64# obj = LRUCache(capacity)
65# param_1 = obj.get(key)
66# obj.put(key,value)