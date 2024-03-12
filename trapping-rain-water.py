class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        lefMax = rightMax = totalWater = 0
        
        while l <= r:   
            if height[l] <= height[r]:
                if height[l] >= lefMax:
                    lefMax = height[l]
                else:
                    totalWater += lefMax - height[l]
                
                l += 1
            else:
                if height[r] >= rightMax:
                    rightMax = height[r]
                else:
                    totalWater += rightMax - height[r]
                
                r -= 1
        
        return totalWater
