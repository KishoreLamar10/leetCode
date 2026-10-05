class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        ans = balance = 0

        for i, char in enumerate(s):
            if char == '(':
                balance += 1
            else:
                balance -= 1
                if s[i -1] == '(':
                    ans += 1 << balance #2 ^ balance
        return ans