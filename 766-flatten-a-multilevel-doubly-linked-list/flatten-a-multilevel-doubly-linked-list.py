"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':
        def get_flattened(head):
            cur = head

            while cur and (cur.next or cur.child):
                if cur.child:
                    nxt = cur.next
                    h, c = get_flattened(cur.child)
                    cur.child = None
                    cur.next = h
                    h.prev = cur

                    if c:
                        c.next = nxt
                    
                    if nxt:
                        nxt.prev = c
                    
                    cur = nxt if nxt else c
                else:
                    cur = cur.next

            return head, cur

        return get_flattened(head)[0]