1class Solution(object):
2    def addBinary(self, a, b):
3        """
4        :type a: str
5        :type b: str
6        :rtype: str
7        """
8        s = []
9        carry = 0
10
11        i = len(a) - 1
12        j = len(b) - 1
13        while i >= 0 or j >= 0 or carry:
14            if i >= 0:
15                carry += int(a[i])
16                i -= 1
17            if j >= 0:
18                carry += int(b[j])
19                j -= 1
20            
21            s.append(str(carry%2))
22            carry = carry // 2
23        
24        return ''.join(reversed(s))