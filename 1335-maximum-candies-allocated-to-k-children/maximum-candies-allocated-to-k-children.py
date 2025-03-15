class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        def is_max_pile(pile):
            max_num_pile = 0

            for candy in candies:
                max_num_pile += candy // pile

            return max_num_pile >= k
                

        left, right = 0, max(candies)

        while left < right:
            mid = (left + right + 1) // 2

            if is_max_pile(mid):
                left = mid
            else:
                right = mid - 1

        return left