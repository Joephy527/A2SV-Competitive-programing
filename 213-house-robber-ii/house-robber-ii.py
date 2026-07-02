class Solution:
    def rob(self, nums: List[int]) -> int:
        def max_robberies(houses):
            n = len(houses)
            dp = [0] * n

            if n == 1:
                return houses[0]

            dp[0], dp[1] = houses[0], max(houses[0], houses[1])

            for idx in range(2, n):
                dp[idx] = max(dp[idx - 1], dp[idx - 2] + houses[idx])

            return dp[-1]

        if len(nums) == 1:
            return nums[0]

        return max(max_robberies(nums[1:]), max_robberies(nums[:-1]))