class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        rangeOfNums = []

        for i in range(len(nums)):
            if i != len(nums) - 1 and not rangeOfNums:
                rangeOfNums.append(str(nums[i]))
                
                if nums[i] + 1 != nums[i + 1]:
                    res.append("->".join(rangeOfNums))
                    rangeOfNums = []
                
                continue

            if i == len(nums) - 1 or nums[i] + 1 != nums[i + 1]:
                rangeOfNums.append(str(nums[i]))
                res.append("->".join(rangeOfNums))
                rangeOfNums = []

        return res
