class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        nums.sort()

        def get_max_pairs(bound):
            l, r = 0, len(nums) - 1
            pair = 0

            while l < r:
                cur = nums[l] + nums[r]

                if cur < bound:
                    pair += r - l
                    l += 1
                else:
                    r -= 1

            return pair

        return get_max_pairs(upper + 1) - get_max_pairs(lower)