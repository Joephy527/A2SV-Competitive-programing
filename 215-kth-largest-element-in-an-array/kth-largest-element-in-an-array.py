class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_num, min_num = max(nums), min(nums)
        n = max_num - min_num + 1
        count = [0] * n

        for num in nums:
            count[num - min_num] += 1

        for i in range(n - 1, -1, -1):
            k -= count[i]

            if k < 1:
                return i + min_num