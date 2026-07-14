class ListNode:
    def __init__(self, val=-1,key=-1,next=None,prev=None,freq=1):
        self.val = val
        self.next = next
        self.prev = prev
        self.key = key
        self.freq = freq

class DoublyLinkedList:
    def __init__(self):
        self.first = ListNode()
        self.last = ListNode()
        self.first.next = self.last
        self.last.prev = self.first

    def remove_node(self, node):
        node.next.prev = node.prev
        node.prev.next = node.next
        node.prev = node.next = None

    def move_to_first(self, node):
        nxt = self.first.next
        self.first.next = node
        nxt.prev = node
        node.next = nxt
        node.prev = self.first

    def remove_last(self, cache):
        if not self.is_empty():
            node = self.last.prev
            self.remove_node(node)
            del cache[node.key]

    def is_empty(self):
        return (
            self.first.next == self.last and
            self.last.prev == self.first
        )

class LFUCache:

    def __init__(self, capacity: int):
        self.cache = {}
        self.freq_map = {1: DoublyLinkedList()}
        self.min_freq = 1
        self.capacity = capacity
        

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        
        node = self.cache[key]
        self.use_node(node)

        return node.val

    def use_node(self, node):
        freq = node.freq
        old_list = self.freq_map[freq]
        old_list.remove_node(node)

        if freq + 1 not in self.freq_map:
            self.freq_map[freq + 1] = DoublyLinkedList()
        
        new_list = self.freq_map[freq + 1]
        node.freq += 1

        if (
            old_list.is_empty() and
            self.min_freq == freq
        ):
            self.min_freq += 1
        
        new_list.move_to_first(node)

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.use_node(node)

            return

        if self.capacity == len(self.cache):
            remove_list = self.freq_map[self.min_freq]
            remove_list.remove_last(self.cache)

        self.min_freq = 1
        node = ListNode(value, key)
        self.cache[key] = node
        doubly_list = self.freq_map[1]
        doubly_list.move_to_first(node)
            


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)