class Solution(object):
    def sumAndMultiply(self, n):
        """
        :type n: int
        :rtype: int
        """

        x = ""
        sums = 0
        for c in str(n):
            if c != '0':
                x += c
                sums += int(c)
                
        if x == "":
            return 0

        return sums * int(x)

        

