# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        dummy = ListNode(0, head)
        prev, cur, nxt = dummy, head, head.next

        while nxt:
            prev.next = nxt
            newNxt = nxt.next
            cur.next = newNxt
            nxt.next = cur

            prev = cur
            cur = cur.next
            nxt = cur.next if cur else None

        return dummy.next
