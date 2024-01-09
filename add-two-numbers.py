# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        n1, n2 = l1, l2
        s1, s2 = "", ""
        
        while n1:
            s1 += str(n1.val)
            n1 = n1.next
        
        while n2:
            s2 += str(n2.val)
            n2 = n2.next

        s1 = s1[::-1]
        s2 = s2[::-1]

        ans = int(s1) + int(s2)
        
        dummy = ListNode()
        tail = dummy

        for c in str(ans)[::-1]:
            tail.next = ListNode(int(c))
            tail = tail.next

        return dummy.next
