class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        i = 0
        n = len(nums)

        while i<n:
            if nums[i] == val:
                n-=1
                nums[i] = nums[n]
            else:
                i +=1
        
        return n
        