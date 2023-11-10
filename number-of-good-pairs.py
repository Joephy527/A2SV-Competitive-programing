class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        ans = 0
        count = Counter(nums)

        for i in count.values():
            ans += sum(range(i))

        return ans
