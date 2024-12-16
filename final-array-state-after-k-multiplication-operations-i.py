class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        heap = [(num, idx) for idx, num in enumerate(nums)]
        heapify(heap)

        for _ in range(k):
            _, minIdx = heappop(heap)

            nums[minIdx] *= multiplier

            heappush(heap, (nums[minIdx], minIdx))

        return nums
