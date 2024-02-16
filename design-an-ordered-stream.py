class OrderedStream:

    def __init__(self, n: int):
        self.idMap = {}
        self.curIdx = 1

    def insert(self, idKey: int, value: str) -> List[str]:
        self.idMap[idKey] = value
        chunk = []

        while self.curIdx in self.idMap:
            chunk.append(self.idMap[self.curIdx])
            self.curIdx += 1

        return chunk


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)
