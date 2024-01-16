# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head.next: return head

        dummy = ListNode(0, head)
        lastSorted, cur = head, head.next

        while cur:
            if cur.val >= lastSorted.val:
                lastSorted = lastSorted.next
            else:
                prev = dummy
                
                while prev.next.val <= cur.val:
                    prev = prev.next

                lastSorted.next = cur.next
                cur.next = prev.next
                prev.next = cur

            cur = lastSorted.next

        return dummy.next
