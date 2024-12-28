class Solution:
    def maxSumOfThreeSubarrays(self, nums: List[int], k: int) -> List[int]:
        sums=[sum(nums[:k])]
        memo = {}
        idx = 0
        starts = []

        for i in range(k, len(nums)):
            sums.append(sums[-1] + nums[i] - nums[i - k])

        def getMax(idx, count):
            if count == 3 or idx > len(nums) - k:
                return 0

            if (idx, count) not in memo:
                include = sums[idx] + getMax(idx + k, count + 1)
                skip = getMax(idx + 1, count)

                memo[(idx, count)] = max(include, skip)

            return memo[(idx, count)]

        while idx <= len(nums) - k and len(starts) < 3:
            include = sums[idx] + getMax(idx + k, len(starts) + 1)
            skip = getMax(idx + 1, len(starts))

            if include >= skip:
                starts.append(idx)
                idx += k
            else:
                idx += 1

        return starts
