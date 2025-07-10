class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        idx_map = {num: idx for idx, num in enumerate(nums1)}
        stack = []
        greater = [-1] * len(nums1)

        for num in nums2:
            while stack and stack[-1] < num:
                smaller = stack.pop()

                if smaller in idx_map:
                    smaller_idx = idx_map[smaller]
                    greater[smaller_idx] = num

            stack.append(num)

        return greater