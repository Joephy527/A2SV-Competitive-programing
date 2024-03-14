class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        count = defaultdict(int)
        count[0] = 1
        s = subArr = 0

        for num in nums:
            s += num
            dif = s - goal
            subArr += count[dif]
            count[s] += 1

        return subArr
