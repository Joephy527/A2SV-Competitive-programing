class Solution:
    def minimumSize(self, nums: List[int], maxOperations: int) -> int:
        def isValidMin(target):
            totalOperations = 0

            for num in nums:
                totalOperations += math.ceil(num / target) - 1

            return totalOperations <= maxOperations
        
        left, right = 1, max(nums)

        while left < right:
            mid = (left + right) // 2

            if isValidMin(mid):
                right = mid
            else:
                left = mid + 1

        return right
