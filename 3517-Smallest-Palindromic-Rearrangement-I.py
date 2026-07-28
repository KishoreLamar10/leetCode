from string import ascii_lowercase
class Solution(object):
    def smallestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        n = len(s)
        freq = Counter(s[:n//2])

        half = []

        for ch in ascii_lowercase:
            if freq[ch] > 0:
                half.append(ch * freq[ch])
        
        half = "".join(half)
        middle = s[n // 2] if n % 2 else ""

        return half + middle + half[::-1]


        