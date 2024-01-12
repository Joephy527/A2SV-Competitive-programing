class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        ans = r

        while l <= r:
            m = (l + r) // 2
            totalTime = 0

            for pile in piles:
                totalTime += math.ceil(float(pile) / m)
            
            if totalTime <= h:
                ans = m
                r = m - 1
            else:
                l = m + 1

        return ans
