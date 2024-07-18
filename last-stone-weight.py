class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] *= -1

        heapify(stones)

        while len(stones) > 1:
            y, x = heappop(stones), heappop(stones)
            dif = (-y) - (-x)

            if dif:
                heappush(stones, -dif)

        return -stones[0] if stones else 0
