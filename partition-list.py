# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        l = dummy
        
        while l and l.next:
            if l.next.val >= x:
                break

            l = l.next

        r = l.next

        while r and r.next:
            if r.next.val < x:
                nxt = l.next
                rnxt = r.next
                r.next = r.next.next
                l.next = rnxt
                rnxt.next = nxt
                l = l.next
            else:
                r = r.next

        return dummy.next
