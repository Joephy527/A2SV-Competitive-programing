class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        count, last, first = [0] * 51, [-1] * 51, [-1] * 51
        prefix = [0]
        max_count = 0

        for idx, num in enumerate(nums):
            prefix.append(prefix[-1] + int(num == k))

            if first[num] == -1:
                first[num] = idx

        for idx, num in enumerate(nums):
            if num == k: continue

            count[num] += 1
            last[num] = idx
            k_count = prefix[idx + 1] - prefix[first[num] + 1]
            net = count[num] - k_count

            if net <= 0:
                first[num] = idx
                count[num] = 1

            max_count = max(max_count, net)

        return max_count + prefix[-1]