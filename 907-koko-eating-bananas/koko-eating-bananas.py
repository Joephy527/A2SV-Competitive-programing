class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def is_valid(speed):
            hour = 0
            
            for pile in piles:
                hour += ceil(pile / speed)

            return hour <= h

        left, right = 1, max(piles)
        min_speed = right

        while left <= right:
            mid = (left + right) // 2

            if is_valid(mid):
                right = mid - 1
                min_speed = mid
            else:
                left = mid + 1

        return min_speed