class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = [0] * len(nums)

        def dp(idx):
            if idx == len(nums):
                return 0

            if not memo[idx]:
                memo[idx] = 1

                for j in range(idx + 1, len(nums)):
                    if nums[j] > nums[idx]:
                        memo[idx] = max(memo[idx], 1 + dp(j))

            return memo[idx]

        maxSequence = 0

        for i in range(len(nums)):
            maxSequence = max(maxSequence, dp(i))

        return maxSequence
