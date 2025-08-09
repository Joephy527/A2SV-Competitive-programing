class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        next_nums2 = [-1] * (max(nums2) + 1)
        next_greater = [-1] * len(nums1)
        stack = []

        for num in nums2:
            while stack and stack[-1] < num:
                next_nums2[stack.pop()] = num

            stack.append(num)

        for idx, num in enumerate(nums1):
            next_greater[idx] = next_nums2[num]

        return next_greater