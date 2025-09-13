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
        def get_flattened(node):
            cur = node
            tail = node

            while cur:
                if cur.child:
                    nxt = cur.next
                    h = cur.child

                    t = get_flattened(cur.child)
                    
                    cur.child = None
                    cur.next = h
                    h.prev = cur

                    if nxt:
                        t.next = nxt
                        nxt.prev = t

                    tail = t
                    cur = nxt
                else:
                    tail = cur
                    cur = cur.next

            return tail

        get_flattened(head)

        return head