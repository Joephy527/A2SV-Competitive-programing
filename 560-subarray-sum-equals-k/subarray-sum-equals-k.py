class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        count[0] = 1
        add = total = 0

        for s in range(len(nums)):
            add += nums[s]
            total += count[add - k]
            count[add] += 1

        return total