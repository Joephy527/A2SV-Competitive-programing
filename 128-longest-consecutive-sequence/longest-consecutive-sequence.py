class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        parents = {num: num for num in nums}
        heights = {num: 1 for num in nums}

        def find(num):
            if num not in parents:
                return float("inf")

            if parents[num] != num:
                parents[num] = find(parents[num])

            return parents[num]

        def union(num):
            root_num, root_num1 = find(num), find(num - 1)

            if (
                float("inf") in (root_num, root_num1) or
                root_num == root_num1
            ):
                return

            if heights[root_num] <= heights[root_num1]:
                heights[root_num1] += heights[root_num]
                parents[root_num] = root_num1
            else:
                heights[root_num] += heights[root_num1]
                parents[root_num1] = root_num

        for num in nums:
            union(num)

        return max(heights.values())