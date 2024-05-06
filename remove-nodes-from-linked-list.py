# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverseList(node):
            prev, cur = None, node

            while cur:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt

            return prev

        newHead = reverseList(head)

        anchor = cur = newHead
        nxt = newHead.next

        while nxt:
            if cur.val <= nxt.val:
                cur.next = nxt
                cur = nxt
            else:
                cur.next = None

            nxt = nxt.next

        return reverseList(anchor)
