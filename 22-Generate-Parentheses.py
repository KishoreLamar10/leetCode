class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        stack = []
        result = []

        def backtrack(opened,closed):
            if closed == opened == n:
                result.append("".join(stack))
            
            if opened < n:
                stack.append('(')
                backtrack(opened+1, closed)
                stack.pop()
            if closed < opened:
                stack.append(')')
                backtrack(opened,closed + 1)
                stack.pop()
        backtrack(0,0)
        return result