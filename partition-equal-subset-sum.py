class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        memo = defaultdict(int)

        def dp(idx, target):
            if idx == len(nums) or target <= 0:
                return not target

            pair = (idx, target)

            if pair not in memo:
                memo[pair] = dp(idx + 1, target - nums[idx]) or dp(idx + 1, target)

            return memo[pair]

        s = sum(nums)

        return not (s % 2) and dp(0, s // 2)
