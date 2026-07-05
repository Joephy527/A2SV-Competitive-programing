# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        heap = []
        dummy = cur = ListNode()

        for idx, linked in enumerate(lists):
            if linked:
                heappush(heap, (linked.val, idx, linked))

        while heap:
            _, idx, node = heappop(heap)
            cur.next = node
            cur = cur.next

            if node.next:
                heappush(heap, (node.next.val, idx, node.next))

        return dummy.next