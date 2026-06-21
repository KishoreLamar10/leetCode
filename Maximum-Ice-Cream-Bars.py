1class Solution(object):
2    def maxIceCream(self, costs, coins):
3        """
4        :type costs: List[int]
5        :type coins: int
6        :rtype: int
7        """
8        max_cost = max(costs)
9
10        freq = [0] * (max_cost + 1)
11
12        for cost in costs:
13            freq[cost] += 1
14
15        ans = 0
16
17        for price in range(1, max_cost + 1):
18            if freq[price] == 0:
19                continue
20
21            can_buy = min(freq[price], coins // price)
22
23            ans += can_buy
24            coins -= can_buy * price
25
26            if coins < price:
27                break
28
29        return ans