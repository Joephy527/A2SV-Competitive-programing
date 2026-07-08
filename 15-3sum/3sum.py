class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()
        
        n = len(nums)
        triplets = []

        def twoSum(idx):
            left, right = idx + 1, n - 1

            while left < right:
                total = nums[left] + nums[right] + nums[idx] 

                if not total:
                    triplets.append([nums[idx], nums[left], nums[right]])

                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left - 1]:
                        left += 1

                    while left < right and nums[right] == nums[right + 1]:
                        right -= 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1

        for i in range(0, n - 2):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            twoSum(i)

        return triplets