class Solution:
    def mincostToHireWorkers(self, quality: List[int], wage: List[int], k: int) -> float:
        ans = float("inf")
        totalQuality = 0
        pairs = [(w / q, q) for q, w in zip(quality, wage)]

        pairs.sort(key=lambda pair: pair[0])
        
        maxHeap = []

        for rate, quality in pairs:
            heappush(maxHeap, -quality)
            totalQuality += quality
            
            if len(maxHeap) > k:
                totalQuality += heappop(maxHeap)
            
            if len(maxHeap) == k:
                ans = min(ans, totalQuality * rate)

        return ans
