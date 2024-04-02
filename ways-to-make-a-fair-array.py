class Solution:
    def waysToMakeFair(self, nums: List[int]) -> int:
        ops = 0
        even, odd = sum(nums[0::2]), sum(nums[1::2])
    
        for i, num in enumerate(nums):
            if not i % 2:
                even -= num
            else:
                odd -= num

            if even == odd:
                ops += 1
            
            if not i % 2:
                odd += num
            else:
                even += num
        
        return ops
