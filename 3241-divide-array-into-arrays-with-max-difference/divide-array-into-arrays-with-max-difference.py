class Solution:
    def divideArray(self, nums: List[int], k: int) -> List[List[int]]:
        nums.sort()

        divided = []

        for i in range(0, len(nums) - 2, 3):
            a, c = nums[i], nums[i + 2]
            
            if c - a > k:
                return []

            divided.append([a, nums[i + 1], c])

        return divided