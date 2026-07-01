1class Solution(object):
2    def findKthLargest(self, nums, k):
3        """
4        :type nums: List[int]
5        :type k: int
6        :rtype: int
7        """
8        heap = nums
9        heapq.heapify(heap)
10
11        while len(heap) > k:
12            heapq.heappop(heap)
13        
14        return heap[0]