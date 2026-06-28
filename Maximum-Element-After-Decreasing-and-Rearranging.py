1class Solution(object):
2    def maximumElementAfterDecrementingAndRearranging(self, arr):
3        """
4        :type arr: List[int]
5        :rtype: int
6        """
7
8        arr.sort()
9
10        n = len(arr)
11
12        arr[0] = 1
13
14        for i in range(1,n):
15            arr[i] = min(arr[i], arr[i-1] + 1)
16        
17
18        return arr[-1]
19        