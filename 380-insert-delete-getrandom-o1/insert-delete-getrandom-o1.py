class RandomizedSet:

    def __init__(self):
        self.idx_map = {}
        self.nums = []

    def insert(self, val: int) -> bool:
        if val in self.idx_map:
            return False

        self.idx_map[val] = len(self.nums)
        self.nums.append(val)

    def remove(self, val: int) -> bool:
        if val in self.idx_map:
            idx = self.idx_map[val]
            self.nums[idx], self.nums[-1] = self.nums[-1], self.nums[idx]
            self.idx_map[self.nums[idx]] = idx
            del self.idx_map[self.nums[-1]]
            self.nums.pop()

            return True

        return False

    def getRandom(self) -> int:
        return self.nums[randint(0, len(self.nums) - 1)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()