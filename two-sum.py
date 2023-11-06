class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        count = {}

        for i, val in enumerate(nums):
            diff = target - val
            if diff in count:
                return [count[diff], i]
            else:
                count[val] = i
        
