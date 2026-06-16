1class Solution(object):
2    def processStr(self, s):
3        """
4        :type s: str
5        :rtype: str
6        """
7
8        res = []
9        n = len(s)
10
11        for i in range(n):
12            ch = s[i]
13
14            if ch == '*':
15                if len(res) != 0:
16                    res.pop()
17            elif ch == '#':
18                res.extend(res)
19            elif ch == '%':
20                res.reverse()
21            elif 'a' <= ch <= 'z':
22                res.append(ch)
23        
24        return ''.join(res)
25        