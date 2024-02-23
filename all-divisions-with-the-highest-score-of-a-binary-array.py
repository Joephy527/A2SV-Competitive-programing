class Solution:
    def maxScoreIndices(self, nums: List[int]) -> List[int]:
        sumOfZeros = 0
        sumOfOnes = maxDivisionScore = nums.count(1)
        distinctIdx = [0]

        for i in range(1, len(nums) + 1):
            if nums[i - 1] == 1:
                sumOfOnes -= 1
            else:
                sumOfZeros += 1

            divisionScore = sumOfOnes + sumOfZeros

            if divisionScore == maxDivisionScore:
                distinctIdx.append(i)

            if divisionScore > maxDivisionScore:
                maxDivisionScore = divisionScore
                distinctIdx = [i]

        return distinctIdx
