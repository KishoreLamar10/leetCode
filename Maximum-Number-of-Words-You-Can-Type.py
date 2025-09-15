class Solution(object):
    def canBeTypedWords(self, text, brokenLetters):
        """
        :type text: str
        :type brokenLetters: str
        :rtype: int
        """
        count = 0
        broken = set(brokenLetters)
        for t in text.split():
            if not any(c in t for c in broken):
                count+=1
        
        return count
        