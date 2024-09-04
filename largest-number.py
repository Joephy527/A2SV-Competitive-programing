class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        nums.sort()

        def isGreater(n, m):
            return n + m > m + n


        for i in range (len (nums)):
            for j in range(i + 1, len(nums)):
                if not isGreater(str(nums[i]), str(nums[j])):
                    nums[i], nums[j] = nums[j], nums[i]

        stringNums = ''.join(map(str, nums))

        return "0" if stringNums[0] == "0" else stringNums
