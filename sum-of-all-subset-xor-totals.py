class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        def helper(arr):
            s = 0

            for num in arr:
                s ^= num

            return s
        
        add = 0
        subSet = []

        def backTrack(idx):
            if idx == len(nums):
                nonlocal add
                add += helper(subSet[:])

                return

            subSet.append(nums[idx])
            backTrack(idx + 1)
            subSet.pop()
            backTrack(idx + 1)

        backTrack(0)

        return add
