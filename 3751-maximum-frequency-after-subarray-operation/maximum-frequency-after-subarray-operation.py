class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        n = len(nums)
        count = [0] * 51
        seen = [-1] * 51
        prefix = [0] * n
        prefix[0] = int(nums[0] == k)
        seen[nums[0]] = 0
        max_k = 0

        for idx in range(1, n):
            num = nums[idx]
            prefix[idx] = prefix[idx - 1] + int(num == k)

            if seen[num] == -1:
                seen[num] = idx

        for idx, num in enumerate(nums):
            if num == k:
                continue

            count[num] += 1
            last_seen = seen[num]
            k_count = prefix[idx] - prefix[last_seen]
            k_freq = count[num] - k_count
            max_k = max(max_k, k_freq)

            if k_freq <= 0:
                seen[num] = idx
                count[num] = 1

        return max_k + prefix[-1]