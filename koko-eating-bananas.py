class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)

        def hoursTaken(num):
            hour = 0
            
            for pile in piles:
                hour += ceil(pile / num)

            return hour

        while l <= r:
            m = (l + r) // 2

            if hoursTaken(m) <= h:
                r = m - 1
            else:
                l = m + 1

        return l
