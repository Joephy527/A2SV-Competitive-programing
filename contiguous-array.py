class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        count = {0: -1}
        maxSubarray = diff = 0
        
        for idx, num in enumerate(nums):
            diff += 1 if num == 1 else -1
            
            if diff in count:
                maxSubarray = max(maxSubarray, idx - count[diff])
            else:
                count[diff] = idx
        
        return maxSubarray
