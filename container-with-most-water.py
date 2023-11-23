class Solution:
    def maxArea(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxWater = 0

        while l < r:
            containerHeight = min(height[l], height[r])
            maxWater = max(maxWater, containerHeight * (r - l))
            
            if containerHeight == height[l]:
                l += 1
            else:
                r -= 1

        return maxWater
