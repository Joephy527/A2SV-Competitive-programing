class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_area = 0

        while left < right:
            min_height = min(height[left], height[right])
            area = min_height * (right - left)
            max_area = max(max_area, area)

            if min_height == height[left]:
                left += 1
            else:
                right -= 1

        return max_area