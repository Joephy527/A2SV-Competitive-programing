class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        ret = []
        for i in nums:
            ret.append(len([j for j in nums if j < i]))
        return ret
