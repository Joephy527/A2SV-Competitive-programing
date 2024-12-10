class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        ans = []
        prefix = [0] * len(nums)

        for i in range(1, len(nums)):
            if nums[i] % 2 == nums[i - 1] % 2:
                prefix[i] = prefix[i - 1] + 1
            else:
                prefix[i] = prefix[i - 1]

        for start, end in queries:
            ans.append(prefix[end] - prefix[start] == 0)

        return ans
