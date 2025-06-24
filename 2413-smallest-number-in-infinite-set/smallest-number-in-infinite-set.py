class SmallestInfiniteSet:

    def __init__(self):
        self.heap = list(range(1, 1001))
        self.seen = set(self.heap)
        heapify(self.heap)

    def popSmallest(self) -> int:
        cur_min = heappop(self.heap)
        self.seen.remove(cur_min)

        return cur_min

    def addBack(self, num: int) -> None:
        if num not in self.seen:
            self.seen.add(num)
            heappush(self.heap, num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)