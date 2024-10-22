
class Solution:
    def rob(self, nums: List[int]) -> int:
        def dp(houses, m):            
            if m == 0:
                return 0
            
            if m == 1:
                return houses[0]
            
            if m == 2:
                return max(houses[0], houses[1])
            
            memo = [0] * m
            memo[0] = houses[0]
            memo[1] = max(houses[0], houses[1])
            
            for i in range(2, m):
                memo[i] = max(memo[i - 1], memo[i - 2] + houses[i])
            
            return memo[-1]
        
        n = len(nums)
        
        if n == 0:
            return 0

        if n == 1:
            return nums[0]

        return max(dp(nums[1:], n - 1), dp(nums[:-1], n - 1))
