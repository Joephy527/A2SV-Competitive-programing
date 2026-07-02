class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n

        if n == 1:
            return nums[0]

        dp[0], dp[1] = nums[0], max(nums[0], nums[1])

        for idx in range(2, n):
            dp[idx] = max(dp[idx - 1], dp[idx - 2] + nums[idx])

        return dp[-1]