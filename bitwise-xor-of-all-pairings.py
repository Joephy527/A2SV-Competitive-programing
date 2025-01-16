class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        xor = 0

        if len(nums2) % 2:
            for num in nums1:
                xor ^= num

        if len(nums1) % 2:
            for num in nums2:
                xor ^= num

        return xor
