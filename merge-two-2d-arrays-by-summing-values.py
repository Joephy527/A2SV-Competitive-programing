class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        merged = []
        p1 = p2 = 0

        while p1 < len(nums1) and p2 < len(nums2):
            id1, val1 = nums1[p1]
            id2, val2 = nums2[p2]
            
            if nums1[p1][0] == nums2[p2][0]:
                merged.append([id1, nums1[p1][1] + nums2[p2][1]])
                p1, p2 = p1 + 1, p2 + 1
            elif nums1[p1][0] > nums2[p2][0]:
                merged.append(nums2[p2])
                p2 += 1
            else:
                merged.append(nums1[p1])
                p1 += 1

        while p1 < len(nums1):
            cur_val = nums1[p1]
            p1 += 1

            merged.append(cur_val)

        while p2 < len(nums2):
            cur_val = nums2[p2]
            p2 += 1

            merged.append(cur_val)

        return merged
