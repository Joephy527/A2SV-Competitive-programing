class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binary_search_right(left, right):
            while left <= right:
                mid = left + (right - left) // 2

                if nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1

            return right

        def binary_search_left(left, right):
            while left <= right:
                mid = left + (right - left) // 2

                if nums[mid] >= target:
                    right = mid - 1
                else:
                    left = mid + 1

            return left

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

        return [binary_search_left(0, idx), binary_search_right(idx, len(nums) - 1)]