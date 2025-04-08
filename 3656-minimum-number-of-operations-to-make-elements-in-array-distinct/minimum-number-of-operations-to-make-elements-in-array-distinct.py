class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        def get_idx():
            seen = set()

            for i in range(len(nums) - 1, -1, -1):
                if nums[i] in seen:
                    return i

                seen.add(nums[i])

            return -1

        idx = get_idx()

        return ceil((idx + 1) / 3)