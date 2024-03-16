class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2

            if nums[m] > target:
                r = m - 1
            elif nums[m] < target:
                l = m + 1
            else:
                L = R = m
                
                while L > 0 and nums[L - 1] == target:
                    L -= 1
                
                while R < len(nums) - 1 and nums[R + 1] == target:
                    R += 1

                return [L, R]

        return [-1, -1]
