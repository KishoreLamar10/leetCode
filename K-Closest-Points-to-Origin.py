1class Solution(object):
2    def kClosest(self, points, k):
3        """
4        :type points: List[List[int]]
5        :type k: int
6        :rtype: List[List[int]]
7        """
8
9        minHeap = []
10        res = []
11        for x,y in points:
12            distance = (x**2) + (y**2)
13            minHeap.append([distance,x,y])
14        
15        heapq.heapify(minHeap)
16
17        while k > 0:
18            distance, x , y = heapq.heappop(minHeap)
19            res.append([x,y])
20            k -= 1
21        
22        return res
23        