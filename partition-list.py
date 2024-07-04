# Definition for singly-linked list.
# class ListNode:
#     def init(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        cur = dummy

        while cur and cur.next:
            if cur.next.val >= x:
                break
                       
            cur = cur.next
        
        nxt = cur.next 

        while nxt and nxt.next:
            if nxt.next.val < x:
                temp = cur.next
                temp_next = nxt.next
                nxt.next = nxt.next.next
                cur.next = temp_next
                temp_next.next = temp
                cur = cur.next
            else:
                nxt= nxt.next

        return dummy.next
