class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        maxSub, curSum = nums[0], 0

        for num in nums:
            if curSum < 0:
                curSum = 0
            curSum += num
            maxSub = max(curSum, maxSub)
        return maxSub
        