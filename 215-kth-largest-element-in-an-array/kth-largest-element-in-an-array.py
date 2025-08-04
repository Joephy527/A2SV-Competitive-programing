class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_num, min_num = max(nums), min(nums)
        n = max_num - min_num + 1
        count = [0] * n

        for num in nums:
            count[num - min_num] += 1

        for num in range(n - 1, -1, -1):
            k -= count[num]

            if k < 1:
                return num + min_num