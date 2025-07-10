class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        count = [0] * 51
        max_k = 0

        for num in nums:
            count[num] = max(count[num], count[k]) + 1

            if num == k:
                max_k += 1

            max_k = max(max_k, count[num])

        return max_k