class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        left, right = 0, len(arr) - 1

        while left <= right:
            mid = (left + right) // 2
            m =  arr[mid]
            l, r = arr[mid - 1], arr[mid + 1]

            if l < m > r:
                return mid
            elif l > arr[mid]:
                right = mid
            else:
                left = mid + 1