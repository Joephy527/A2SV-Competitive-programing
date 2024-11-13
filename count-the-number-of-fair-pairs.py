class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()
        pairs = 0

        def binarySearch(left, target):
            right = len(nums) - 1
            
            while left <= right:
                mid = (left + right) // 2

                if nums[mid] < target:
                    left = mid + 1
                elif nums[mid] >= target:
                    right = mid - 1

            return left

        for i in range(len(nums)):
            low = binarySearch(i + 1, lower - nums[i])
            high = binarySearch(i + 1, upper - nums[i] + 1)

            pairs += high - low

        return pairs
