class MedianFinder:

    def __init__(self):
        self.maxHeap, self.minHeap = [], []

    def addNum(self, num):
        if not self.maxHeap or num <= -self.maxHeap[0]:
            heappush(self.maxHeap, -num)
        else:
            heappush(self.minHeap, num)

        if len(self.maxHeap) > len(self.minHeap) + 1:
            heappush(self.minHeap, -heappop(self.maxHeap))
        elif len(self.minHeap) > len(self.maxHeap):
            heappush(self.maxHeap, -heappop(self.minHeap))

    def findMedian(self):
        if len(self.maxHeap) == len(self.minHeap):
            return (-self.maxHeap[0] + self.minHeap[0]) / 2.0
        else:
            return -self.maxHeap[0]
