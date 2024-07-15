class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        heap = []
        pairs = []
        
        for num in nums1:
            heappush(heap, (num + nums2[0], num, 0))
        
        while heap and k:
            _, num1, num2Idx = heappop(heap)
            pairs.append([num1, nums2[num2Idx]])
            
            if num2Idx + 1 < len(nums2):
                heappush(heap, (num1 + nums2[num2Idx + 1], num1, num2Idx + 1))

            k -= 1
        
        return pairs
