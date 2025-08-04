class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)

        def is_shippable(weight):
            day = 1
            s = 0

            for w in weights:
                if s + w > weight:
                    s = 0
                    day += 1

                s += w

            return day <= days

        while left <= right:
            mid = left + (right - left) // 2

            if is_shippable(mid):
                right = mid - 1
            else:
                left = mid + 1

        return left