1class Solution(object):
2    def largestAltitude(self, gain):
3        """
4        :type gain: List[int]
5        :rtype: int
6        """
7        curr = 0
8        highest = 0
9
10        for g in gain:
11            curr += g
12            highest = max(highest,curr)
13
14        return highest