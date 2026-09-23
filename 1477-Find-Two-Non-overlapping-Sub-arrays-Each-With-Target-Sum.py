class Solution(object):
    def minSumOfLengths(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        n = len(arr)

        res, total, i = n+1, 0, 0

        dp = [n] * (n + 1)

        for j in range(n):
            total += arr[j]

            while total > target:
                total -= arr[i]
                i += 1
            
            dp[j + 1] = dp[j]

            if total == target:
                Len = j - i + 1
                res = min(res, Len + dp[i])
                dp[j + 1] = min(dp[j], Len)
        
        return -1 if res == n+1 else res