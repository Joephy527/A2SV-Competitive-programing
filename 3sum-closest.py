class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = float("inf")
        
        for i in range(len(nums)):
            cur = nums[i]
            l, r = i + 1, len(nums) - 1

            while l < r:
                s = cur + nums[l] + nums[r]

                if s > target:
                    r -= 1
                else:
                    l += 1

                if abs(s - target) < abs(closest - target):
                    closest = s

        return closest
