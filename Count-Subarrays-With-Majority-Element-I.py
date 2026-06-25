1class Solution(object):
2    def countMajoritySubarrays(self, nums, target):
3        """
4        :type nums: List[int]
5        :type target: int
6        :rtype: int
7        """
8        n = len(nums)
9        ans = 0
10        for i in range(n):
11            count = 0
12            for j in range(i,n):
13                if nums[j] == target:
14                    count += 1
15                
16                length = j - i + 1
17                
18                if (count*2) > length:
19                    ans += 1
20        
21
22        return ans
23
24        
25
26        