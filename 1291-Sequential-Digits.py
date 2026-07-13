class Solution(object):
    def sequentialDigits(self, low, high):
        """
        :type low: int
        :type high: int
        :rtype: List[int]
        """

        digits = "123456789"
        res = []

        for length in range(2,10):
            for start in range(0, 10 - length):
                num = int(digits[start: start+length])
                if low <= num <= high:
                    res.append(num)
        
        return sorted(res)
        