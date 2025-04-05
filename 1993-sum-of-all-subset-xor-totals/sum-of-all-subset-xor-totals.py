class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def back_track(idx, prev_xor):
            if idx == len(nums):
                return prev_xor

            cur_xor = prev_xor ^ nums[idx]
            
            return (
                back_track(idx + 1, cur_xor) +
                back_track(idx + 1, prev_xor)
            )

        return back_track(0, 0)