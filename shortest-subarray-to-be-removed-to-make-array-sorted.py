class Solution:
    def findLengthOfShortestSubarray(self, arr: List[int]) -> int:
        n = len(arr)
        left, right = 0, n - 1

        while left < n - 1 and arr[left + 1] >= arr[left]:
            left += 1

        while right > 0 and arr[right - 1] <= arr[right]:
            right -= 1

        if left == n - 1: return 0

        minSubArray = min(n - left -1, right)
        l, r = 0, right

        while l <= left and r < n:
            if arr[l] <= arr[r]:
                minSubArray = min(minSubArray, r - l - 1)
                l += 1
            else:
                r += 1

        return minSubArray
