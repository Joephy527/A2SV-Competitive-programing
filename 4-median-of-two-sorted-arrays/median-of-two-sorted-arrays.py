class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        n, m = len(nums1), len(nums2)
        left, right = 0, n

        while left <= right:
            i = (left + right) // 2
            j = ((n + m + 1) // 2) - i

            a_left = nums1[i - 1] if i > 0 else float("-inf")
            a_right = nums1[i] if i < n else float("inf")
            b_left = nums2[j - 1] if j > 0 else float("-inf")
            b_right = nums2[j] if j < m else float("inf")

            if a_left <= b_right and b_left <= a_right:
                l, r = max(a_left, b_left), min(a_right, b_right)
                if (m + n) % 2:
                    return float(l)
                
                return (l + r) / 2

            if a_left > b_right:
                right = i - 1
            else:
                left = i + 1