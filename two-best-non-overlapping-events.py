class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort(key=lambda x: x[0])
        
        heap = []
        maxVal = maxSum = 0

        for start, end, val in events:
            while heap and heap[0][0] < start:
                maxVal = max(maxVal, heap[0][1])
                heappop(heap)

            maxSum = max(maxSum, maxVal + val)

            heappush(heap, (end, val))

        return maxSum
