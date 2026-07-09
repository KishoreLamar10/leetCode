class Solution(object):
    def sumAndMultiply(self, s, queries):
        """
        :type s: str
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        MOD = 10**9 + 7
        n = len(s)

        nonZeroCount = [0] * (n + 1)
        digits = []

        for i in range(n):

            nonZeroCount[i + 1] = nonZeroCount[i]

            if s[i] != "0":
                digits.append(int(s[i]))
                nonZeroCount[i + 1] += 1

        k = len(digits)

        prefixNum = [0] * (k + 1)
        prefixSum = [0] * (k + 1)
        power10 = [1] * (k + 1)

        for i in range(k):

            prefixNum[i + 1] = (
                prefixNum[i] * 10 + digits[i]
            ) % MOD

            prefixSum[i + 1] = (
                prefixSum[i] + digits[i]
            )

            power10[i + 1] = (
                power10[i] * 10
            ) % MOD

        answer = []

        for left, right in queries:

            compressedLeft = nonZeroCount[left]

            compressedRight = nonZeroCount[right + 1]

            length = compressedRight - compressedLeft

            x = (
                prefixNum[compressedRight]
                - prefixNum[compressedLeft]
                * power10[length]
            ) % MOD

            digitSum = (
                prefixSum[compressedRight]
                - prefixSum[compressedLeft]
            )

            answer.append(
                (x * digitSum) % MOD
            )

        return answer