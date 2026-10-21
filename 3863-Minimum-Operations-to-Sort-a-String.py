class Solution:
    def minOperations(self, s: str) -> int:
        n = len(s)
        mins = maxs = s[0]
        isSorted = 1

        for i in range(1,n):
            if s[i] < s[i-1]:
                isSorted = 0
            mins = min(mins,s[i])
            maxs = max(maxs,s[i])
        
        if isSorted: return 0
        if n == 2: return -1
        if s[0] == mins or s[-1] == maxs:
            return 1
        
        for i in range(1, n-1):
            if s[i] == mins or s[i] == maxs:
                return 2
        return 3