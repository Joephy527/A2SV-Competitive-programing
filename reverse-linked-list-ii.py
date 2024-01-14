# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        lPrev = dummy
        l = dummy.next
        lCount = 1

        while lCount < left:
            lPrev = l
            l = l.next
            lCount += 1

        r = l
        rNext = l.next
        rCount = 0
        while rCount < right - left:
            r = rNext
            rNext = rNext.next
            rCount += 1

        cur = l
        prev = None
        while cur != rNext:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp
        
        lPrev.next = r
        l.next = rNext

        return dummy.next
