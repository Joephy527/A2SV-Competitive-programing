# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        maxDis, minDis = 0, float("inf")
        cur = head
        prev = first = None
        dis = 0

        def isCritical(node):
            return (node.val < node.next.val > node.next.next.val or
                node.val > node.next.val < node.next.next.val)

        while cur.next.next:
            dis += 1
            
            if isCritical(cur):
                if not first:
                    first = dis
                else:
                    maxDis = dis - first
                    minDis = min(minDis, dis - prev)
                
                prev = dis

            cur = cur.next

        maxDis = maxDis if maxDis else -1
        minDis = minDis if minDis != float("inf") else -1

        return [minDis, maxDis]
