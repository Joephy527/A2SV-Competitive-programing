class SmallestInfiniteSet:

    def __init__(self):
        self.heap = []
        self.seen = set()
        self.num = 1

    def popSmallest(self) -> int:
        if self.heap:
            smallest = heappop(self.heap)
            self.seen.remove(smallest)
        else:
            smallest = self.num
            self.num += 1

        return smallest

    def addBack(self, num: int) -> None:
        if self.num > num and num not in self.seen:
            heappush(self.heap, num)
            self.seen.add(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)