class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        dic = {num: i for i, num in enumerate(nums2)}
        res = []

        for num in nums1:
            idx = dic[num]
            greater = -1
            for i in range(idx + 1, len(nums2)):
                if nums2[i] > num:
                    greater = nums2[i]
                    break

            res.append(greater)

        return res
