1class Solution(object):
2    def angleClock(self, hour, minutes):
3        """
4        :type hour: int
5        :type minutes: int
6        :rtype: float
7        """
8        hourangle = ((hour % 12) * 30) + (0.5 * minutes) 
9        minangle = minutes * 6
10
11        diff = abs(hourangle - minangle)
12
13        return min(diff, 360 - diff)
14        