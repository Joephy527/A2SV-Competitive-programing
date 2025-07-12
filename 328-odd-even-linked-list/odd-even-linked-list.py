# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return
        
        even, odd = ListNode(), ListNode()
        even_node, odd_node = even, odd
        cur = head
        idx = 1

        while cur:
            node = ListNode(cur.val)

            if idx % 2:
                odd_node.next = node
                odd_node = odd_node.next
            else:
                even_node.next = node
                even_node = even_node.next
            
            cur = cur.next
            idx += 1

        odd_node.next = even.next

        return odd.next