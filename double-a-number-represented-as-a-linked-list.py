# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(node):
            prev, cur = None, node

            while cur:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt

            return prev

        head = reverse(head)
        cur = head
        rem = 0

        while cur:
            new = (cur.val * 2) + rem

            if len(str(new)) == 2:
                rem = int(str(new)[0])
            else:
                rem = 0

            cur.val = new % 10
            cur = cur.next

        if rem:
            cur = head

            while cur.next:
                cur = cur.next

            cur.next = ListNode(rem)

        return reverse(head)
