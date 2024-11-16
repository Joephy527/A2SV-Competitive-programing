class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        if k == 1:
            return nums

        count = 1
        result = [-1] * (len(nums) - k + 1)

        for idx in range(len(nums) - 1):
            if nums[idx] + 1 == nums[idx + 1]:
                count += 1
            else:
                count = 1

            if count >= k:
                result[idx -k + 2] = nums[idx + 1]

        return result
