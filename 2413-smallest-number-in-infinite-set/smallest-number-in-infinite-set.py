class SmallestInfiniteSet:

    def __init__(self):
        self.heap = list(range(1, 1001))
        self.seen = [True] * 1001
        
        heapify(self.heap)

    def popSmallest(self) -> int:
        cur_min = heappop(self.heap)
        self.seen[cur_min] = False

        return cur_min

    def addBack(self, num: int) -> None:
        if not self.seen[num]:
            self.seen[num] = True
            heappush(self.heap, num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)