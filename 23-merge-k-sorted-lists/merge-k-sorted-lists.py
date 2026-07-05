# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        dummy = cur = ListNode()

        for linked in lists:
            while linked:
                heappush(heap, linked.val)
                linked = linked.next

        while heap:
            val = heappop(heap)
            cur.next = ListNode(val)
            cur = cur.next

        return dummy.next