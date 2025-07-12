class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        stack = []
        greater = [-1] * len(nums)

        for idx, num in enumerate(nums):
            while stack and nums[stack[-1]] < num:
                greater[stack.pop()] = num

            stack.append(idx)

        for num in nums:
            while stack and nums[stack[-1]] < num:
                greater[stack.pop()] = num

        return greater