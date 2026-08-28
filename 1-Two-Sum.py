class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hashmap:
                return [i, hashmap[diff]]
            hashmap[nums[i]] = i 
        return []