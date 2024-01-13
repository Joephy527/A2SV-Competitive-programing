# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or not k: return head

        length = 1
        tail = head

        while tail.next:
            length += 1
            tail = tail.next

        k = k % length

        tail.next = newTail = head

        for i in range(length - k - 1):
            newTail = newTail.next

        node = newTail.next
        newTail.next = None

        return node
