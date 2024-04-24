class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        nextGreater = {}
        greater = []

        for num in nums2:
            while stack and stack[-1] < num:
                nextGreater[stack.pop()] = num

            stack.append(num)

        while stack:
            nextGreater[stack.pop()] = -1

        for num in nums1:
            greater.append(nextGreater[num])

        return greater
