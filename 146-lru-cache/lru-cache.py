class LRUCache:

    def __init__(self, capacity: int):
        self.dict = {}
        self.capacity = capacity
        self.queue = deque()

    def get(self, key: int) -> int:
        if key in self.dict:
            val = self.dict[key]
            self.queue.remove(key)
            self.queue.append(key)
            
            return val

        return -1


    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            self.queue.remove(key)

        self.dict[key] = value
        
        self.queue.append(key)

        if len(self.queue) > self.capacity:
            del self.dict[self.queue.popleft()]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)