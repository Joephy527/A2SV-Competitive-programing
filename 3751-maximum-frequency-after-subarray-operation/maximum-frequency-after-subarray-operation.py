class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        count = defaultdict(int)
        k_count = max_k = 0

        for num in nums:
            count[num] = max(count[num], k_count) + 1

            if num == k:
                max_k += 1
                k_count += 1

            max_k = max(max_k, count[num])

        return max_k