class Solution:
    def minimizedMaximum(self, n: int, quantities: List[int]) -> int:
        heap = [(-q, q, 1) for q in quantities]
        heapify(heap)

        for _ in range(n - len(quantities)):
            _, quantity, stores = heappop(heap)
            
            stores += 1
            ratio = quantity / stores
            
            heappush(heap, (-ratio, quantity, stores))

        ratio, _, _ = heappop(heap)

        return ceil(-ratio)
