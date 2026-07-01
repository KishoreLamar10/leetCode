1class Solution(object):
2    def leastInterval(self, tasks, n):
3        """
4        :type tasks: List[str]
5        :type n: int
6        :rtype: int
7        """
8        count = Counter(tasks)
9        maxHeap = [-cnt for cnt in count.values()]
10        heapq.heapify(maxHeap)
11
12        time = 0
13        q = deque() #-cnt, idletime
14
15        while maxHeap or q:
16            time += 1
17
18            if maxHeap:
19                cnt = 1 + heapq.heappop(maxHeap)
20                if cnt:
21                    q.append([cnt, time + n])
22            
23            if q and q[0][1] == time:
24                heapq.heappush(maxHeap, q.popleft()[0])
25        
26        return time