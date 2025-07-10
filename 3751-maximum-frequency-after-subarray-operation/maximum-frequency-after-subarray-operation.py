class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = defaultdict(int)
        seen = {}
        prefix = [0] * n
        prefix[0] = int(nums[0] == k)
        max_k = 0

        for idx in range(n):
            prefix[idx] = prefix[idx - 1] + int(nums[idx] == k)

        for idx, num in enumerate(nums):
            if num not in seen:
                seen[num] = idx

        for idx, num in enumerate(nums):
            if num != k:
                count[num] += 1
                last_seen = seen[num]
                k_count = prefix[idx] - prefix[last_seen]
                k_freq = count[num] - k_count
                max_k = max(max_k, k_freq)

                if k_freq <= 0:
                    seen[num] = idx
                    count[num] = 1

        return max_k + prefix[-1]