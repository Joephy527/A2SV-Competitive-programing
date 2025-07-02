class MedianFinder:

    def __init__(self):
        self.max_heap = []
        self.min_heap = []

    def addNum(self, num: int) -> None:
        if len(self.max_heap) > len(self.min_heap):
            if -self.max_heap[0] > num:
                cur = -heapreplace(self.max_heap, -num)
            else:
                cur = num

            heappush(self.min_heap, cur)
        else:
            if self.min_heap and self.min_heap[0] < num:
                cur = heapreplace(self.min_heap, num)
            else:
                cur = num
            
            heappush(self.max_heap, -cur)
            
            

    def findMedian(self) -> float:
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0] / 1
        elif len(self.max_heap) < len(self.min_heap):
            return self.min_heap[0] / 1
        else:
            return (self.min_heap[0] - self.max_heap[0]) / 2


# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()