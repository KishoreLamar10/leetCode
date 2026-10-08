class Solution(object):
    def removeOuterParentheses(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ''
        level = 0
        
        for c in s:
            if c == '(':
                if level > 0:
                    res += c
                level += 1
            else:
                level -= 1
                if level > 0:
                    res += c
        
        return res