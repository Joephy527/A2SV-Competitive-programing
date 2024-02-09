class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        minCount = len(nums) // 3
        countNums = Counter(nums)
        majorityElements = []

        for num in countNums:
            if countNums[num] > minCount:
                majorityElements.append(num)

        return majorityElements
