class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prifixMul = [nums[0]]
        prifixMulRe = [nums[-1]]
        res = []

        for i in range(1, len(nums)):
            mul = prifixMul[-1] * nums[i]
            prifixMul.append(mul)

        for i in range(len(nums) - 2, -1, -1):
            mul = prifixMulRe[-1] * nums[i]
            prifixMulRe.append(mul)

        prifixMulRe.reverse()

        for i in range(len(nums)):
            if i == 0:
                res.append(prifixMulRe[1])
            elif i == len(nums) - 1:
                res.append(prifixMul[len(nums) - 2])
            else:
                ans = prifixMul[i - 1] * prifixMulRe[i + 1]
                res.append(ans)

        return res
