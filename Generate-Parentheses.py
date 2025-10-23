class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        stack = []
        result = []

        def backtrack(opened, closed):

            if opened == closed == n:
                result.append("".join(stack))
                return
            
            if opened < n:
                stack.append('(')
                backtrack(opened + 1, closed)
                stack.pop()
            
            if closed < opened:
                stack.append(')')
                backtrack(opened, closed + 1)
                stack.pop()
        
        backtrack(0,0)
        return result
        