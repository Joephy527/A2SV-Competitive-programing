class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        idx_map = {}

        for idx, num in enumerate(nums):
            dif = target - num

            if dif in idx_map:
                return [idx_map[dif], idx]

            idx_map[num] = idx