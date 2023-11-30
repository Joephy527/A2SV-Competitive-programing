class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        count[0] = 1
        ans = s = 0

        for num in nums:
            s += num
            diff = s - k
            ans += count[diff]
            count[s] += 1

        return ans
