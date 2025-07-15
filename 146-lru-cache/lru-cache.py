class ListNode:
    def __init__(self, val = -1, key = -1):
        self.key = key
        self.val = val
        self.prev = None
        self.nxt = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}
        self.head = self.tail = ListNode()
        self.head.nxt = self.tail
        self.tail.prev = self.head


    def remove(self, node: ListNode) -> None:
        node.prev.nxt = node.nxt
        node.nxt.prev = node.prev


    def insert(self, node: ListNode) -> None:
        prev = self.tail.prev
        self.tail.prev = node
        prev.nxt = node
        node.nxt = self.tail
        node.prev = prev


    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1

        node = self.cache[key]

        self.remove(node)
        self.insert(node)

        return node.val


    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.remove(node)
        else:
            node = ListNode(value, key)
            self.cache[key] = node

        self.insert(node)

        if len(self.cache) > self.cap:
            node = self.head.nxt
            self.remove(node)
            del self.cache[node.key]



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)