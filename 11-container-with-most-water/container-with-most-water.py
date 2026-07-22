class Solution:
    def maxArea(self, height: List[int]) -> int:
        n = len(height)
        left, right = 0, n - 1
        max_water = 0

        while left < right:
            left_height = height[left]
            right_height = height[right]
            width = right - left

            if left_height < right_height:
                min_height = left_height
                left += 1
            else:
                min_height = right_height
                right -= 1

            max_water = max(
                max_water,
                min_height * width
            )

        return max_water