class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        countOnes = maxOnes = 0

        for num in nums:
            if num == 0:
                maxOnes = max(maxOnes, countOnes)
                countOnes = 0
            else:
                countOnes += 1

        return max(maxOnes, countOnes)