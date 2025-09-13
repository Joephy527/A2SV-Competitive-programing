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
                    h, c = get_flattened(cur.child)
                    cur.child = None
                    cur.next = h
                    h.prev = cur

                    if nxt:
                        c.next = nxt
                        nxt.prev = c

                    tail = c
                    cur = nxt
                else:
                    tail = cur
                    cur = cur.next

            return node, tail

        if not head:
            return None

        return get_flattened(head)[0]