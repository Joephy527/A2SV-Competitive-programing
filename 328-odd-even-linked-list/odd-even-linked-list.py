# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if (
            head and
            head.next and
            head.next.next
        ):
            odd, even = head, head.next
            even_node = even

            while even_node and even_node.next:
                odd.next = odd.next.next
                odd = odd.next
                even_node.next = even_node.next.next
                even_node = even_node.next

            odd.next = even

        return head