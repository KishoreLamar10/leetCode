class Solution(object):
    def braceExpansionII(self, expression):
        """
        :type expression: str
        :rtype: List[str]
        """
        answer = set()

        def dfs(s):
            r = s.find('}')

            if r == -1:
                answer.add(s)
                return
            l = s.rfind('{',0,r)

            left = s[:l]
            right = s[r + 1:]

            inside = s[l + 1:r]

            for part in inside.split(','):
                dfs(left + part + right)
        
        dfs(expression)
        return sorted(answer)