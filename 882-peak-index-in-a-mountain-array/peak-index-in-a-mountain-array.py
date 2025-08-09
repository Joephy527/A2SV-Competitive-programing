class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left, right = 0, len(arr)

        while left <= right:
            mid = left + (right - left) // 2

            if (
                0 < mid < len(arr) -1 and
                arr[mid - 1] < arr[mid] > arr[mid + 1]
            ):
                return mid
            elif 0 < mid:
                if arr[mid - 1] > arr[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                if arr[mid + 1] > arr[mid]:
                    left = mid + 1
                else:
                    right = mid - 1