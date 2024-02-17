class RandomizedSet:

    def __init__(self):
        self.indexMap = {}
        self.valueList = []

    def insert(self, val: int) -> bool:
        if val not in self.indexMap:
            self.indexMap[val] = len(self.valueList)
            self.valueList.append(val)
            
            return True

    def remove(self, val: int) -> bool:
        if val in self.indexMap:
            toBeRemoved = self.indexMap[val]
            
            self.indexMap[self.valueList[-1]] = toBeRemoved
            self.valueList[-1], self.valueList[toBeRemoved] = self.valueList[toBeRemoved], self.valueList[-1]
            
            del self.indexMap[val]
            self.valueList.pop()

            return True

    def getRandom(self) -> int:
        return choice(self.valueList)


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
