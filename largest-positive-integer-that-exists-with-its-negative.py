class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        nums.sort()
        l, r = 0, len(nums) - 1

        while l < r:
            if nums[l] == nums[r]:
                break
            
            neg = abs(nums[l])
            
            if neg < nums[r]:
                r -= 1
            elif neg > nums[r]:
                l += 1
            else:
                return nums[r]

        return -1
