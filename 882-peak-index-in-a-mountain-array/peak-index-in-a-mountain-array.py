class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left, right = 0, len(arr) - 1

        while left <= right:
            mid = (left + right) // 2
            m =  arr[mid]
            l, r = arr[max(mid - 1, 0)], arr[min(mid + 1, len(arr) - 1)]

            if l < m > r:
                return mid
            elif l > arr[mid]:
                right = mid - 1
            else:
                left = mid + 1