class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        p, n = 0, 1
        rearrange = [0] * len(nums)

        for num in nums:
            if num > 0:
                rearrange[p] = num
                p += 2
            else:
                rearrange[n] = num
                n += 2

        return rearrange
