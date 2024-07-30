class Solution:
    def totalCost(self, costs: List[int], k: int, candidates: int) -> int:
        totalCost = 0
        l, r = 0, len(costs) - 1
        heap = []

        heapify(heap)

        for _ in range(candidates):
            heappush(heap, [costs[l], 0])
            l += 1

        for _ in range(candidates):
            if l <= r:
                heappush(heap, [costs[r], 1])
                r -= 1

        while k and heap:
            cost, direction = heappop(heap)
            totalCost += cost

            if l <= r:
                if not direction:
                    heappush(heap, [costs[l], 0])
                    l += 1
                else:
                    heappush(heap, [costs[r], 1])
                    r -= 1

            k -= 1

        return totalCost
