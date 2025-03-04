class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        ans = [0] * len(nums)
        less_idx = 0
        greater_idx = len(nums) - 1

        for i, j in zip(range(len(nums)), range(len(nums) - 1, -1, -1)):
            if nums[i] < pivot:
                ans[less_idx] = nums[i]
                less_idx += 1
            if nums[j] > pivot:
                ans[greater_idx] = nums[j]
                greater_idx -= 1

        while less_idx <= greater_idx:
            ans[less_idx] = pivot
            less_idx += 1

        return ans
