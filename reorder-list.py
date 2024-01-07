# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        arr = []
        node = head
        
        while node:
            arr.append(node)
            node = node.next
        
        l, r = 0, len(arr)-1
        tail = head
        
        while l < r:
            arr[l].next = arr[r]
            l += 1
            
            if l == r: 
                tail = arr[r]
                break
                
            arr[r].next = arr[l]
            r -= 1
            
            tail = arr[l]
        
        if tail:
            tail.next= None
