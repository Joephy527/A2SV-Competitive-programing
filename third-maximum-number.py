class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        sortedNums = sorted(set(nums))

        if len(sortedNums) < 3:
            return sortedNums[-1]

        return sortedNums[-3]
