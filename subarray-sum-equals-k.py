class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dict1 = defaultdict(int)
        dict1[0] = 1
        ans = 0

        # turn nums to prefix sum
        for i in range(1, len(nums)):
            nums[i] += nums[i - 1]

        for num in nums:
            if num - k in dict1:
                ans = ans + dict1[num - k]
            dict1[num] += 1

        return ans
