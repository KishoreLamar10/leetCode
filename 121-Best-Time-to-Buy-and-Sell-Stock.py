class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l,r = 0, 1 
        n = len(prices)
        profit = 0
        while r < n:
            if prices[r] > prices[l]:
                profit = max(profit, prices[r] - prices[l])
                r += 1
            else:
                l = r
                r += 1
        
        return profit
