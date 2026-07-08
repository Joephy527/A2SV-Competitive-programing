class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n, m = len(nums1), len(nums2)

        if n > m:
            nums1, nums2 = nums2, nums1
            n, m = m, n

        total_length = n + m
        half = (total_length + 1) // 2

        left = 0
        right = n

        while left <= right:
            partition_one = (left + right) // 2
            partition_two = half - partition_one

            left_one_max = (
                float("-inf")
                if partition_one == 0
                else nums1[partition_one - 1]
            )
            right_one_min = (
                float("inf")
                if partition_one == n
                else nums1[partition_one]
            )

            left_two_max = (
                float("-inf")
                if partition_two == 0
                else nums2[partition_two - 1]
            )
            right_two_min = (
                float("inf")
                if partition_two == m
                else nums2[partition_two]
            )

            if (
                left_one_max <= right_two_min
                and left_two_max <= right_one_min
            ):
                left_max = max(left_one_max, left_two_max)
                right_min = min(right_one_min, right_two_min)

                if total_length % 2 == 1:
                    return float(left_max)

                return (left_max + right_min) / 2

            if left_one_max > right_two_min:
                right = partition_one - 1
            else:
                left = partition_one + 1