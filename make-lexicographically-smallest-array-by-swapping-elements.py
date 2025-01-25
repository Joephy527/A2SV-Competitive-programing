class Solution:
    def lexicographicallySmallestArray(self, nums: List[int], limit: int) -> List[int]:
        groups = []
        group_idx = {}
        smallest = []

        for num in sorted(nums):
            if (
                not groups or
                abs(num - groups[-1][-1]) > limit
            ):
                groups.append(deque())

            groups[-1].append(num)
            group_idx[num] = len(groups) - 1

        for num in nums:
            idx = group_idx[num]
            smallest.append(groups[idx].popleft())

        return smallest
