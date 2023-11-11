class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        res = []

        for i in range(n):
            res.append(nums[i])
            res.append(nums[n])
            n += 1

        return res
