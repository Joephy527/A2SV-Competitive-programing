class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cur_sum = subarray = 0
        sums = defaultdict(int)
        sums[0] = 1

        for num in nums:
            cur_sum += num
            diff = cur_sum - k
            subarray += sums[diff]
            sums[cur_sum] += 1

        return subarray