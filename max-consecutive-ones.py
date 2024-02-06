class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        countOnes = maxOnes = 0

        for num in nums:
            if num == 0:
                countOnes = 0
            else:
                countOnes += 1
                maxOnes = max(maxOnes, countOnes)

        return maxOnes
