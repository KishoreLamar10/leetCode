1class Solution(object):
2    def maxIceCream(self, costs, coins):
3        """
4        :type costs: List[int]
5        :type coins: int
6        :rtype: int
7        """
8        xMin = xMax = max(costs)
9        freq = [0] * (xMax + 1)
10        for x in costs:
11            freq[x] += 1
12            xMin = min(xMin, x)
13        cnt = 0
14        for x, f in enumerate(freq[xMin:], start=xMin):
15            if f == 0:
16                continue
17            buy = min(coins // x, f)
18            if buy == 0:
19                break
20            cnt += buy
21            coins -= buy * x
22        return cnt