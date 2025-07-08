class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def get_hour(amount):
            hour = 0

            for pile in piles:
                hour += ceil(pile / amount)

            return hour

        left, right = 1, max(piles)
        k = 0

        while left <= right:
            mid = left + (right - left) // 2

            hour = get_hour(mid)

            if hour <= h:
                k = mid
                right = mid - 1
            else:
                left = mid + 1

        return k