1# Definition for singly-linked list.
2# class ListNode(object):
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution(object):
7    def addTwoNumbers(self, l1, l2):
8        """
9        :type l1: Optional[ListNode]
10        :type l2: Optional[ListNode]
11        :rtype: Optional[ListNode]
12        """
13
14        dummy = ListNode()
15        cur = dummy
16
17        carry = 0
18
19        while l1 or l2 or carry:
20            v1 = l1.val if l1 else 0
21            v2 = l2.val if l2 else 0
22
23            val = v1 + v2 + carry
24            carry = val//10
25            val = val%10
26
27            cur.next = ListNode(val)
28
29            cur = cur.next
30            l1 = l1.next if l1 else None
31            l2 = l2.next if l2 else None
32        
33        return dummy.next
34        