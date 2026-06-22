1class Solution(object):
2    def maxNumberOfBalloons(self, text):
3        """
4        :type text: str
5        :rtype: int
6        """
7        b=a=l=o=n=0
8        for c in text:
9            if c=='b':
10                b+=1
11            elif c=='a':
12                a+=1
13            elif c=='l':
14                l+=1
15            elif c=='o':
16                o+=1
17            elif c=='n':
18                n+=1
19
20        return min(b,a,n,l//2,o//2)