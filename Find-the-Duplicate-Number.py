1class Solution(object):
2    def findDuplicate(self, nums):
3        """
4        :type nums: List[int]
5        :rtype: int
6        """
7        slow,fast = 0,0
8
9        while True:
10            slow = nums[slow]
11            fast = nums[nums[fast]]
12
13            if slow == fast:
14                break
15        
16        slow2 = 0
17
18        while True:
19            slow = nums[slow]
20            slow2 = nums[slow2]
21
22            if slow == slow2:
23                return slow
24        