# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        head = ListNode(float("-inf"))

        for node in lists:
            cur_node = node
            prev_head, cur_head = head, head.next

            while cur_node:
                while cur_head and cur_head.val <= cur_node.val:
                    prev_head = cur_head
                    cur_head = cur_head.next

                prev_head.next = cur_node
                prev_head = cur_node
                nxt = cur_node.next
                cur_node.next = cur_head
                cur_node = nxt

        return head.next