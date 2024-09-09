class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        oneElement = 0
        threeElements = 0
        
        for num in nums:
            oneElement = (oneElement ^ num) & (~threeElements)
            threeElements = (threeElements ^ num) & (~oneElement)

        return oneElement
