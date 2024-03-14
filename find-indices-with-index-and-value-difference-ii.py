class Solution:
    def findIndices(self, nums: List[int], indexDifference: int, valueDifference: int) -> List[int]:
        minIdx, maxIdx = 0, 0
        
        for i in range(indexDifference, len(nums)):
            if nums[i - indexDifference] < nums[minIdx]:
                minIdx = i - indexDifference
            
            if nums[i - indexDifference] > nums[maxIdx]:
                maxIdx = i - indexDifference
            
            if nums[i] - nums[minIdx] >= valueDifference:
                return [minIdx, i]
            
            if nums[maxIdx] - nums[i] >= valueDifference:
                return [maxIdx, i]
        
        return [-1, -1]
