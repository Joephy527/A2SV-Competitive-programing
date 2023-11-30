class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        count[0] = 1
        s = ans = 0

        for num in nums:
            s += num
            rem = s % k
            ans += count[rem]
            count[rem] += 1

        return ans
