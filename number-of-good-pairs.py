class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        goodPairs = 0
        count = Counter(nums)

        for amount in count.values():
            goodPairs += sum(range(amount))

        return goodPairs
