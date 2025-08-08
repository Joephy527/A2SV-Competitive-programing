class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        sum_1, sum_2 = sum(nums1), sum(nums2)
        zero_1, zero_2 = nums1.count(0), nums2.count(0)
        max_1, max_2 = sum_1 + zero_1, sum_2 + zero_2

        if not zero_1 and not zero_2:
            return sum_1 if sum_1 == sum_2 else -1
        elif not zero_1:
            return sum_1 if max_2 <= sum_1 else -1
        elif not zero_2:
            return sum_2 if max_1 <= sum_2 else -1

        return max(max_1, max_2)