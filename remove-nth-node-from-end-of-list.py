# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        node, tail = dummy, head
        
        for i in range(n):
            tail = tail.next

        while tail:
            node = node.next
            tail = tail.next

        node.next = node.next.next

        return dummy.next
