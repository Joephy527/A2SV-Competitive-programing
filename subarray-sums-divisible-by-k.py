class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        dic = defaultdict(int)
        dic[0] = 1
        cur = ans = 0

        for num in nums:
            cur += num
            rem = cur % k
            ans += dic[rem]
            dic[rem] += 1

        return ans
