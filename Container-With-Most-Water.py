class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        l,r = 0,len(height) - 1
        res=0
        while l<r:
            area = (r-l) * min(height[r],height[l])

            if(height[r]> height[l]):
                l+=1
            else:
                r-=1
            res = max(area,res)
        return res