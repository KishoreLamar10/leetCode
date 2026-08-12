class Solution(object):
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = nums[0]

        mins, maxs = 1,1

        for num in nums:
            tmp = maxs * num
            maxs = max(maxs* num, mins * num, num)
            mins = min(tmp, mins* num, num)

            res = max(maxs, mins, res)
        
        return res