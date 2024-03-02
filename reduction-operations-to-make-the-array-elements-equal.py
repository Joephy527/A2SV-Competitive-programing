class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        totalOperations = op = 0
        prev = nums[0]
        
        for num in nums:
            if num != prev:
                op += 1
            
            totalOperations += op
            prev = num

        return totalOperations
