class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        left, right = max(weights), sum(weights)
        weight = right

        def is_shippable(weight):
            day = 1
            s = 0

            for w in weights:
                if s + w <= weight:
                    s += w
                else:
                    s = w
                    day += 1

            return day <= days

        while left <= right:
            mid = left + (right - left) // 2

            if is_shippable(mid):
                weight = mid
                right = mid - 1
            else:
                left = mid + 1

        return weight