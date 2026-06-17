1# Definition for singly-linked list.
2# class ListNode(object):
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution(object):
7    def reverseKGroup(self, head, k):
8        """
9        :type head: Optional[ListNode]
10        :type k: int
11        :rtype: Optional[ListNode]
12        """
13        dummy = ListNode(0,head)
14        groupprev = dummy
15
16        while True:
17            kth = self.getKth(groupprev,k)
18            if not kth:
19                break
20            groupnext = kth.next
21        
22            prev, curr = groupnext, groupprev.next
23
24            while curr != groupnext:
25                tmp = curr.next
26                curr.next = prev
27                prev = curr
28                curr = tmp
29            
30            tmp = groupprev.next
31            groupprev.next = kth
32            groupprev = tmp
33    
34        return dummy.next
35
36    def getKth(self,curr,k):
37        while curr and k>0:
38            curr = curr.next
39            k-=1
40            
41        return curr
42        