class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        a = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] < nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
        for i in range(len(nums)):
            if nums[i] == target:
                a.append(i)
        return a
