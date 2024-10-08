class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}

        def dp(idx, count):
            if idx == len(nums):
                if count == target:
                    return 1
                else: 
                    return 0
            
            if (idx, count) in memo:
                return memo[(idx, count)]

            
            include = dp(idx + 1, count + nums[idx])
            execlude=dp(idx + 1, count - nums[idx])
            
            memo[(idx, count)] = include + execlude
            
            return  memo[(idx,count)]
        
        return dp(0,0)
