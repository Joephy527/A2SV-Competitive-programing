class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        minBanana = r

        while l <= r:
            k = (l + r) // 2
            time = 0

            for pile in piles:
                time += ceil(pile / k)

            if time <= h:
                minBanana = k
                r = k - 1
            else:
                l = k + 1

        return minBanana
