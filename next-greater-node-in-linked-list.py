# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        res = []
        stack = []
        greater = defaultdict(int)
        cur = head

        while cur:
            while stack and stack[-1].val < cur.val:
                greater[stack.pop()] = cur.val

            stack.append(cur)

            cur = cur.next

        cur = head

        while cur:
            res.append(greater[cur])
            cur = cur.next

        return res
