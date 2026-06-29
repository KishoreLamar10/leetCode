1class KthLargest(object):
2
3    def __init__(self, k, nums):
4        """
5        :type k: int
6        :type nums: List[int]
7        """
8        self.minHeap = nums
9        self.k = k
10
11        heapq.heapify(self.minHeap)
12        while len(self.minHeap) > k:
13            heapq.heappop(self.minHeap)
14        
15
16    def add(self, val):
17        """
18        :type val: int
19        :rtype: int
20        """
21        heapq.heappush(self.minHeap, val)
22        if len(self.minHeap) > self.k:
23            heapq.heappop(self.minHeap)
24        
25        return self.minHeap[0]
26        
27
28
29# Your KthLargest object will be instantiated and called as such:
30# obj = KthLargest(k, nums)
31# param_1 = obj.add(val)