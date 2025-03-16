class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def is_min_time(minutes):
            cur_cars = 0

            for rank in ranks:
                cur_cars += int(sqrt(minutes // rank))

            return cur_cars >= cars

        left, right = 1, min(ranks) * cars * cars

        while left <= right:
            mid = (left + right) // 2

            if is_min_time(mid):
                right = mid - 1
            else:
                left = mid + 1

        return left
