class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] < 10: continue

            nums.append(int(str(nums[i])[::-1]))

        return len(set(nums))
