class Solution(object):
    def kClosest(self, points, k):
        """
        :type points: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """

        minHeap = []
        res = []

        for x,y in points:
            distance = (x**2) + (y**2)
            minHeap.append([distance,x,y])
        heapq.heapify(minHeap)

        while k>0:
            distance,x,y = heapq.heappop(minHeap)
            res.append([x,y])
            k -=1
        return res
        