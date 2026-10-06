class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """       
        if len(s) != len(t):
            return False
        
        seen = {}

        for c in s:
            seen[c] = seen.get(c,0) + 1
        for c in t:
            if c not in seen or seen[c] == 0:
                return False
            seen[c] -= 1
        return True


        