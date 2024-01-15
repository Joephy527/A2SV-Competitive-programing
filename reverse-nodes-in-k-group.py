# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0, head)
        nodePrev = dummy

        while True:
            nodeK = self.getnodeK(nodePrev, k)

            if not nodeK:
                break

            nodeNext = nodeK.next

            prev, curr = nodeK.next, nodePrev.next

            while curr != nodeNext:
                tmp = curr.next
                curr.next = prev
                prev = curr
                curr = tmp

            tmp = nodePrev.next
            nodePrev.next = nodeK
            nodePrev = tmp

        return dummy.next

    def getnodeK(self, curr, k):
        while curr and k > 0:
            curr = curr.next
            k -= 1
        return curr
