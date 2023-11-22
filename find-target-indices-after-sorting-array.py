class Solution:
    def targetIndices(self, nums: List[int], target: int) -> List[int]:
        helper = [0] * (max(nums) + 1)
        for num in nums:
            helper[num] += 1

        sortedArr = []
        for i, count in enumerate(helper):
            while count:
                sortedArr.append(i)
                count -= 1

        res = []
        for idx, val in enumerate(sortedArr):
            if val == target:
                res.append(idx)

        return res
