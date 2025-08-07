# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if (
            not head or
            not head.next
        ):
            return head

        cur = head
        length = 1

        while cur.next:
            length += 1
            cur = cur.next

        cur.next = head
        k %= length
        cur = head

        for _ in range(length - k - 1):
            cur = cur.next

        new_head = cur.next
        cur.next = None

        return new_head