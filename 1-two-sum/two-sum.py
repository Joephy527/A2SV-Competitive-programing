class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx_map = {}

        for i, num in enumerate(nums):
            dif = target - num

            if dif in idx_map:
                return [idx_map[dif], i]

            idx_map[num] = i