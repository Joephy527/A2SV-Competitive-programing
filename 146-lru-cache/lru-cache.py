class LRUCache:

    def __init__(self, capacity: int):
        self.dict = {}
        self.cap = capacity
        self.left, self.right = ListNode(), ListNode()
        self.left.next, self.right.prev = self.right, self.left

    def get(self, key: int) -> int:
        if key in self.dict:
            node = self.dict[key]
            val = node.val
            
            self.remove(node)
            self.insert(node)

            return val

        return -1


    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            node = self.dict[key]
            node.val = value
            self.remove(node)
        else:
            node = ListNode(value, key)
            self.dict[key] = node
        
        self.insert(node)

        if len(self.dict) > self.cap:
            to_be_removed = self.left.next
            self.remove(to_be_removed)
            del self.dict[to_be_removed.key]

    
    def insert(self, node):
        prev = self.right.prev
        self.right.prev = node
        prev.next = node
        node.prev = prev
        node.next = self.right

    
    def remove(self, node):
        nxt = node.next
        prev = node.prev
        nxt.prev = prev
        prev.next = nxt


class ListNode:
    def __init__(self, val = 0, key = -1):
        self.val = val
        self.key = key
        self.prev = None
        self.next = None



# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)