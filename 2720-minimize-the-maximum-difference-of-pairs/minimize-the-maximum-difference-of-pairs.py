class Solution:
    def minimizeMax(self, nums: List[int], p: int) -> int:
        nums.sort()

        left, right = 0, nums[-1] - nums[0]

        def count_valid_pairs(m):
            pairs = i = 0

            while i < len(nums) - 1:
                if nums[i + 1] - nums[i] <= m:
                    pairs += 1
                    i += 1
                
                i += 1

            return pairs >= p

        while left < right:
            mid = (left + right) // 2

            if count_valid_pairs(mid):
                right = mid
            else:
                left = mid + 1

        return right