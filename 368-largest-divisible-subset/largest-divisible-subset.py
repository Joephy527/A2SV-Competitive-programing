class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        memo = {}
        max_subset = []
        
        def back_track(idx):
            if idx == len(nums):
                return []

            if idx not in memo:
                cur_subset = [nums[idx]]

                for j in range(idx + 1, len(nums)):
                    if nums[j] % nums[idx]:
                        continue

                    max_j = back_track(j)

                    if len(max_j) >= len(cur_subset):
                        cur_subset = [nums[idx]] + max_j

                memo[idx] = cur_subset

            return memo[idx]

        for i in range(len(nums)):
            max_i = back_track(i)

            if len(max_i) > len(max_subset):
                max_subset = max_i

        return max_subset