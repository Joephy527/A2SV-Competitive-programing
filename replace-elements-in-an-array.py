class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        indexMap = {}

        for idx, num in enumerate(nums):
            indexMap[num] = idx

        for num, replace in operations:
            nums[indexMap[num]] = replace
            indexMap[replace] = indexMap[num]

        return nums
