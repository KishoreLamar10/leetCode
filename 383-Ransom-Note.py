class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        hashmap = {}

        if len(ransomNote) > len(magazine): return False

        for char in magazine:
            if char not in hashmap:
                hashmap[char] = 1
            else:
                hashmap[char] += 1
        
        for char in ransomNote:
            if char in hashmap and hashmap[char] > 0:
                hashmap[char] -= 1
            else:
                return False
        
        return True

        
                