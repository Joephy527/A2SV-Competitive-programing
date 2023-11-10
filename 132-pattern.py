class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        if len(nums) < 3: return False

        stack = []
        comp = float("-inf")

        nums = nums[::-1]

        for i in nums:
            if i < comp: return True

            while stack and i > stack[-1]:
                comp = stack.pop()

            stack.append(i)
