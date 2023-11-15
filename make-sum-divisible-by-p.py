class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        if sum(nums) < p: return -1
        target = sum(nums) % p

        if target == 0: return 0

        dic = defaultdict(int)
        dic[0] = -1
        cur = 0
        minWin = len(nums)

        for i in range(len(nums)):
            cur = (cur + nums[i]) % p
            if (cur - target) % p in dic:
                minWin = min(minWin, i - dic[(cur - target) % p])

            dic[cur] = i

        return minWin if minWin != len(nums) else -1
