class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        memo = {n - 1: 0}

        def dp(idx):
            if idx not in memo:
                if idx >= n or not nums[idx]:
                    return float("inf")
                
                jump = float("inf")

                for i in range(1, nums[idx] + 1):
                    jump = min(jump, dp(idx + i))

                memo[idx] = jump + 1

            return memo[idx]

        min_jump = dp(0)
        
        return min_jump if min_jump != float("inf") else 0