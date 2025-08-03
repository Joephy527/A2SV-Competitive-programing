class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binary_search(isLeft = True):
            left, right = 0, len(nums) - 1
            pos = -1

            while left <= right:
                mid = left + (right - left) // 2

                if nums[mid] > target:
                    right = mid - 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    pos = mid
                    
                    if isLeft:
                        right = mid - 1
                    else:
                        left = mid + 1

            return pos

        return [binary_search(), binary_search(False)]