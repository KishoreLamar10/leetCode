class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        res = []
        nums.sort()

        for i, value in enumerate(nums):

            if(i > 0 and value == nums[i-1]):
                continue
            
            l,r = i+1, len(nums) -1 

            while l<r:
                threesum = value + nums[l] + nums[r]

                if threesum < 0:
                    l+=1
                elif threesum > 0:
                    r-=1
                else:
                    res.append([value,nums[l],nums[r]])
                    l+=1
                    while l<r and nums[l] == nums[l-1]:
                        l+=1
        return res