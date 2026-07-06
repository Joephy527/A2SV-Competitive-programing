# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        cur_one, cur_two, cur_sum = l1, l2, dummy
        remain = 0

        while cur_one or cur_two or remain:
            val = remain
            val += cur_one.val if cur_one else 0
            val += cur_two.val if cur_two else 0

            remain = val // 10
            val = val % 10
            cur_sum.next = ListNode(val)
            
            cur_sum = cur_sum.next
            cur_one = cur_one.next if cur_one else None
            cur_two = cur_two.next if cur_two else None

        return dummy.next