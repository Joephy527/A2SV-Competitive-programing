class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        minSubArray = float("inf")
        s = 0
        prefixHeap = []

        for idx, num in enumerate(nums):
            s += num

            if s >= k:
                minSubArray = min(minSubArray, idx + 1)

            while prefixHeap and s - prefixHeap[0][0] >= k:
                _, minIdx = heappop(prefixHeap)
                minSubArray = min(minSubArray, idx - minIdx)

            heappush(prefixHeap, (s, idx))

        return minSubArray if minSubArray != float("inf") else -1
