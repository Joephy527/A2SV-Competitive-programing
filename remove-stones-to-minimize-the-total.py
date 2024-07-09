class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        heap = [-p for p in piles]
        heapify(heap)

        for _ in range(k):
            cur = floor(heappop(heap) / 2)
            heappush(heap, cur)

        return -sum(heap)
