class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans = []

        for i in range(len(nums)):
            if nums[i] == nums[i - 1] and i > 0:
                continue

            l, r = i + 1, len(nums) - 1

            while l < r:
                Sum = nums[i] + nums[l] + nums[r]
                if Sum == 0:
                    ans.append([nums[i], nums[l], nums[r]])
                    l += 1

                    while nums[l] == nums[l - 1] and l < r:
                        l += 1
                elif Sum < 0:
                    l += 1
                else:
                    r -= 1

        return ans
