class Solution(object):
    def maxDepth(self, s):
        """
        :type s: str
        :rtype: int
        """
        depth = 0
        res = 0

        for c in s:
            if c == ')':
                depth -= 1
                continue
            if c != '(':
                continue
            depth += 1
            if depth > res:
                res = depth
        return res

        