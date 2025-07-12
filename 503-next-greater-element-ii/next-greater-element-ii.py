class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        nums += nums
        stack = []
        greater = [-1] * n

        for idx, num in enumerate(nums):
            while stack and nums[stack[-1]] < num:
                greater[stack.pop()] = num

            if idx < n:
                stack.append(idx)

        return greater