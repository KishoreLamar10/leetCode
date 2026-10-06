class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        n = len(s)

        for i in range(len(s)):
            if s[i] == '(' or s[i] == '{' or s[i] == '[':
                stack.append(s[i])
            else:
                if not stack:
                    return False
                top = stack.pop()
                if s[i] == ')' and top != '(':
                    return False
                if s[i] == '}' and top!= '{':
                    return False
                if s[i] == ']' and top != '[':
                    return False
        
        return len(stack) == 0