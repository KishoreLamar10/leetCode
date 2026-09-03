class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res = majority = 0

        for num in nums:
            if majority == 0:
                res = num
            majority += 1 if res == num else -1
        
        return res