class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        count = Counter(nums1)
        intersection = []

        for num in nums2:
            if count[num]:
               intersection.append(num)
               count[num] -= 1

        return intersection
