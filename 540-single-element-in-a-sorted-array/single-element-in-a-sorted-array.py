class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        left, right = 0, n - 1

        while left <= right:
            mid = left + (right - left) // 2
            cur = nums[mid]

            if (
                mid > 0 and
                nums[mid] == nums[mid - 1]
            ):
                if mid % 2:
                    left = mid + 1
                else:
                    right = mid - 1
            elif (
                mid < n - 1 and
                nums[mid] == nums[mid + 1]
            ):
                if mid % 2:
                    right = mid - 1
                else:
                    left = mid + 1
            else:
                return nums[mid]