class SmallestInfiniteSet:

    def __init__(self):
        self.heap = [i for i in range(1, 1001)]
        self.set = [True] * 1001

        heapify(self.heap)

    def popSmallest(self) -> int:
        smallest = heappop(self.heap)
        self.set[smallest] = False

        return smallest

    def addBack(self, num: int) -> None:
        if not self.set[num]:
            self.set[num] = True
            heappush(self.heap, num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
