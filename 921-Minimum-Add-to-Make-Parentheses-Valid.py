class Solution(object):
    def minAddToMakeValid(self, s):
        """
        :type s: str
        :rtype: int
        """
        opens = add = 0

        for c in s:
            if c == '(':
                opens += 1
            else:
                if opens > 0 :
                    opens -= 1
                else:
                    add += 1
        return add + opens