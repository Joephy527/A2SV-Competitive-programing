# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (
            not head or
            not head.next
        ):
            return head

        even, odd = head, head.next
        odd_org = head.next

        while odd and odd.next:
            even.next = odd.next
            odd.next = odd.next.next
            even = even.next
            odd = odd.next

        even.next = odd_org

        return head