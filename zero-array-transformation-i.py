class Solution:
    def isZeroArray(self, nums: List[int], queries: List[List[int]]) -> bool:
        prefix = [0] * (len(nums) + 1)

        for left, right in queries:
            prefix[left] += 1
            prefix[right + 1] -= 1
            
        for i in range(len(prefix) - 1):
            prefix[i + 1] += prefix[i]
            
            if prefix[i] < nums[i]:
                return False

        return True
