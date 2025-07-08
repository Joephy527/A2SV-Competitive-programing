class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binary_search(is_left = False):
            left, right = 0, len(nums) - 1
            idx = -1

            while left <= right:
                mid = left + (right - left) // 2

                if nums[mid] > target:
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    idx = mid
                    if is_left:
                        right = mid - 1
                    else:
                        left = mid + 1

            return idx

        start, end = binary_search(True), binary_search()

        return [start, end]