class Solution:
    def getLargestOutlier(self, nums: List[int]) -> int:
        s = sum(nums)
        count = Counter(nums)
        max_num = float("-inf")

        for num in count:
            special = s - num
            
            if (
                not special % 2 and
                special // 2 in count and
                (
                    num != special // 2 or
                    count[num] > 1
                )
            ):
                max_num = max(max_num, num)

        return max_num