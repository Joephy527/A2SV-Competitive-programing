class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        s = sum(nums)

        if s % 2: return False

        target = s // 2
        memo = [False] * (target + 1)
        memo[0] = True

        for num in nums:
            for t in range(target, num - 1, -1):
                memo[t] = memo[t] or memo[t - num]

        return memo[-1]