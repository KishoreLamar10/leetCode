1class Solution(object):
2    def processStr(self, s, k):
3        """
4        :type s: str
5        :type k: int
6        :rtype: str
7        """
8
9        n = len(s)
10        length = [0] * n
11        cur = 0
12
13        for i in range(n):
14            ch = s[i]
15            if 'a' <= ch <= 'z':
16                cur += 1
17            elif ch == '*':
18                if cur > 0:
19                    cur -= 1
20            elif ch == '#':
21                cur = min(cur * 2, 10**15)
22            
23            length[i] = cur
24        
25        if k >= cur:
26            return '.'
27        
28        for i in range(n-1,-1,-1):
29            ch = s[i]
30
31            if 'a' <= ch <= 'z':
32                if length[i] - 1 == k:
33                    return ch
34            elif ch == '#':
35                prev = length[i] // 2
36                if k >= prev:
37                    k -= prev
38            elif ch == '%':
39                k = length[i] - 1 - k
40        
41        return '.'
42        