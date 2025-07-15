class SmallestInfiniteSet:

    def __init__(self):
        self.heap = []
        self.min_int = 1
        self.seen = [False] * 1001
        

    def popSmallest(self) -> int:
        if self.heap:
            cur_min = heappop(self.heap)
        else:
            cur_min = self.min_int
            self.min_int += 1

        self.seen[cur_min] = False

        return cur_min

    def addBack(self, num: int) -> None:
        if (
            num < self.min_int and
            not self.seen[num]
        ):
            heappush(self.heap, num)
            self.seen[num] = True


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)