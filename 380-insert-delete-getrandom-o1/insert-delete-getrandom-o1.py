class RandomizedSet:

    def __init__(self):
        self.idx_map = {}
        self.array = []

    def insert(self, val: int) -> bool:
        if val in self.idx_map:
            return False

        self.idx_map[val] = len(self.array)
        self.array.append(val)

        return True

    def remove(self, val: int) -> bool:
        if val not in self.idx_map:
            return False

        idx = self.idx_map[val]
        last_val = self.array[-1]
        self.array[idx] = last_val
        self.array[-1] = val
        self.idx_map[last_val] = idx

        del self.idx_map[self.array.pop()]

        return True

    def getRandom(self) -> int:
        n = len(self.array) - 1
        
        return self.array[randint(0, n)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()