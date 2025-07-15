class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left, right = 0, len(arr) - 1

        while left <= right:
            mid = left + (right - left) // 2

            if (
                mid > 0 and mid < len(arr) - 1 and
                arr[mid - 1] < arr[mid] > arr[mid + 1]
            ):
                return mid
            elif mid > 0:
                if arr[mid - 1] > arr[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if arr[mid] > arr[mid + 1]:
                    right = mid - 1
                else:
                    left = mid + 1