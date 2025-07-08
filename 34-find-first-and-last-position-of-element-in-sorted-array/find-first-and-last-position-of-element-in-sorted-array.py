class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binary_search():
            left, right = 0, len(nums) - 1
            
            while left <= right:
                mid = left + (right - left) // 2

                if nums[mid] > target:
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    return mid

            return -1

        idx = binary_search()

        if idx == -1: return [-1, -1]

        return [bisect_left(nums, nums[idx]), bisect_right(nums, nums[idx]) - 1]