class Solution(object):
    MOD = 10**9 + 7
    def distinctSubseqII(self, s):
        """
        :type s: str
        :rtype: int
        """

        total = 0
        dp = [0] * 26

        for c in s:
            c = ord(c) - 97
            new = total + 1 - dp[c]
            total = (total + new) % self.MOD
            dp[c] = (dp[c] + new) % self.MOD
        return total