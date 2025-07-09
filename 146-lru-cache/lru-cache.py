class ListNode:
    def __init__(self, val=0, key=-1, prev=None, nxt=None):
        self.key = key
        self.prev = prev
        self.next = nxt
        self.val = val


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity
        self.head, self.tail = ListNode(), ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head

    def remove(self, node: ListNode) -> None:
        node.prev.next = node.next
        node.next.prev = node.prev


    def insert(self, node: ListNode) -> None:
        prev = self.tail.prev
        prev.next = node
        node.next = self.tail
        node.prev = prev
        self.tail.prev = node


    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        self.remove(node)
        self.insert(node)
        
        return node.val


    def put(self, key: int, value: int) -> None:
        if key not in self.cache:
            node = ListNode(val=value, key=key)
            self.cache[key] = node
        else:
            node = self.cache[key]
            node.val = value
            self.remove(node)
        
        self.insert(node)

        if len(self.cache) > self.cap:
            node = self.head.next
            self.remove(node)
            del self.cache[node.key]



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)