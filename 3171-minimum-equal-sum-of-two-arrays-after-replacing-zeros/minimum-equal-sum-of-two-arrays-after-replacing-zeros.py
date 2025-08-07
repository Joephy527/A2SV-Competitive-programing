class Solution:
    def minSum(self, nums1: List[int], nums2: List[int]) -> int:
        sum_1, sum_2 = sum(nums1), sum(nums2)
        zero_1, zero_2 = nums1.count(0), nums2.count(0)

        print(sum_1, zero_1)
        print(sum_2, zero_2)

        if (
            (sum_1 > sum_2 and not zero_2) or
            (sum_1 < sum_2 and not zero_1) or
            (sum_1 == sum_2 and (
                (zero_1 and not zero_2) or
                (zero_2 and not zero_1)
            ))
        ):
            return -1

        if sum_1 > sum_2:
            if zero_2 > sum_1 - sum_2 and not zero_1:
                return -1
        elif sum_1 < sum_2:
            if zero_1 > sum_2 - sum_1 and  not zero_2:
                return -1

        return max(sum_1 + zero_1, sum_2 + zero_2)