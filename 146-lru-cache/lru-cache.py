class ListNode:
    def __init__(self, val: int = -1, key: int = -1, prev: ListNode = None, nxt: ListNode = None):
        self.val = val
        self.next = nxt
        self.prev = prev
        self.key = key

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}
        self.first, self.last = ListNode(), ListNode()
        self.first.next = self.last
        self.last.prev = self.first

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]
        node.prev.next, node.next.prev = node.next, node.prev
        nxt = self.first.next
        node.next, node.prev = nxt, self.first
        nxt.prev, self.first.next = node, node


        return node.val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            
            node.prev.next = node.next
            node.next.prev = node.prev
        else:
            node = ListNode(value, key)
            self.cache[key] = node

        nxt = self.first.next

        node.next, node.prev = nxt, self.first
        nxt.prev, self.first.next = node, node

        if len(self.cache) > self.capacity:
            node = self.last.prev
            node.prev.next, node.next.prev = node.next, node.prev
            del self.cache[node.key]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)