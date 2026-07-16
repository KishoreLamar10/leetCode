class Solution(object):
    def gcd(self, a, b):
            if b == 0:
                return a
            return self.gcd(b, a%b)

    def gcdSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
    
        n = len(nums)
        prefix = [0] * n

        maxi = 0
        for i in range(n):
            maxi = max(maxi, nums[i])
            prefix[i] = self.gcd(nums[i], maxi)
        
        prefix.sort()
        res = 0     
        for i in range(n//2):
            res += self.gcd(prefix[i], prefix[n - 1 - i])
        
        return res
        
        