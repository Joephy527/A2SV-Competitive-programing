class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        countMap = Counter(nums)
        majority = countEle = 0

        for num in countMap:
            if countEle < countMap[num]:
                countEle = countMap[num]
                majority = num

        return majority
