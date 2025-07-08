# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur = dummy
        rem = 0
        length1 = length2 = 0
        cur1, cur2 = l1, l2

        while cur1 or cur2 or rem:
            cur_val = rem
            cur_val += cur1.val if cur1 else 0
            cur_val += cur2.val if cur2 else 0

            rem = cur_val // 10
            
            cur.next = ListNode(cur_val % 10)
            cur = cur.next
            
            cur1 = cur1.next if cur1 else cur1
            cur2 = cur2.next if cur2 else cur2

        return dummy.next