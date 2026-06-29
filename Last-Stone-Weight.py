1class Solution(object):
2    def lastStoneWeight(self, stones):
3        """
4        :type stones: List[int]
5        :rtype: int
6        """
7        heap = [-x for x in stones]
8        heapq.heapify(heap)
9
10        while len(heap) > 1:
11            first = heapq.heappop(heap)
12            second = heapq.heappop(heap)
13
14            if first != second:
15                heapq.heappush(heap, first - second)
16
17        return -heap[0] if heap else 0
18        