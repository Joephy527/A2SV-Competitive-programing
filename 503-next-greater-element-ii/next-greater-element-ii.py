class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        stack = []
        greater = [-1] * n

        for i in range(2 * n):
            num = nums[i % n]
            
            while stack and num > nums[stack[-1]]:
                greater[stack.pop()] = num

            stack.append(i % n)

        return greater