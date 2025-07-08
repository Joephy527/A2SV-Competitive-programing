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

        while cur1 and cur2:
            cur_val = cur1.val + cur2.val + rem
            cur_node = ListNode(cur_val % 10)
            rem = cur_val // 10
            cur.next = cur_node
            cur = cur.next
            cur1 = cur1.next
            cur2 = cur2.next

        while cur1:
            cur_val = cur1.val + rem
            cur_node = ListNode(cur_val % 10)
            rem = cur_val // 10
            cur.next = cur_node
            cur = cur.next
            cur1 = cur1.next

        while cur2:
            cur_val = cur2.val + rem
            cur_node = ListNode(cur_val % 10)
            rem = cur_val // 10
            cur.next = cur_node
            cur = cur.next
            cur2 = cur2.next

        if rem:
            cur.next = ListNode(rem)

        return dummy.next