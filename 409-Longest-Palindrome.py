class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        odd_count = 0
        
        d = {}
        
        for c in s:
            if c in d:
                d[c] += 1
            else:
                d[c] = 1
            if d[c] % 2 == 1:
                odd_count += 1
            else:
                odd_count -= 1
        
        if odd_count > 1:
            return len(s) - odd_count + 1
        else:
            return len(s)