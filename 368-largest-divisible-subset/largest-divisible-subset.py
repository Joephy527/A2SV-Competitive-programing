class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        
        memo = {}
        
        def back_track(idx, prev):
            if idx == len(nums):
                return []

            if (idx, prev) not in memo:
                cur_subset = back_track(idx + 1, prev)

                if not nums[idx] % prev:
                    max_idx = back_track(idx + 1, nums[idx])

                    if len(max_idx) >= len(cur_subset):
                        cur_subset = [nums[idx]] + max_idx

                memo[(idx, prev)] = cur_subset

            return memo[(idx, prev)]

        return back_track(0, 1)