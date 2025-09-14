class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()

        divided = []

        for i in range(0, len(nums) - 2, 3):
            if nums[i + 2] - nums[i] > k:
                return []

            divided.append(nums[i: i + 3])

        return divided