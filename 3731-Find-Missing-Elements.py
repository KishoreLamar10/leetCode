class Solution(object):
    def findMissingElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        seen = set(nums)

        mn = min(nums)
        mx = max(nums)

        ans = []

        for x in range(mn, mx + 1):
            if x not in seen:
                ans.append(x)
        
        return ans