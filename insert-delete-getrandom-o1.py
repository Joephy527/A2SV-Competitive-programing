class RandomizedSet:

    def __init__(self):
        self.val_map = {}
        self.val_list = []

    def insert(self, val: int) -> bool:
        if val in self.val_map:
            return False
        
        self.val_map[val] = len(self.val_list)
        self.val_list.append(val)

        return True

    def remove(self, val: int) -> bool:
        if val not in self.val_map:
            return False

        idx = self.val_map[val]
        last_val = self.val_list[-1]
        self.val_list[idx] = last_val
        self.val_map[last_val] = idx

        del self.val_map[val]
        self.val_list.pop()

        return True

    def getRandom(self) -> int:
        n = len(self.val_list) - 1
        return self.val_list[randint(0, n)]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
