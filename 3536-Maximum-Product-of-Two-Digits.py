class Solution(object):
    def maxProduct(self, n):
        """
        :type n: int
        :rtype: int
        """
        first = 0
        second = 0

        while n>0:
            digit = n % 10

            if digit >= first:
                second = first
                first = digit
            elif digit > second:
                second = digit
            
            n = n // 10
        
        return first * second