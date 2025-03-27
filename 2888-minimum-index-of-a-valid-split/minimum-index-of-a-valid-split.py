class Solution:
    def minimumIndex(self, nums: List[int]) -> int:
        count = defaultdict(int)
        max_num = nums[0]
        max_num_count = 0

        for num in nums:
            count[num] += 1

            if count[num] > count[max_num]:
                max_num = num

        for idx, num in enumerate(nums):
            max_num_count += num == max_num
            num_count = count[max_num] - max_num_count

            if (max_num_count > (idx + 1) // 2 and
                num_count > (len(nums) - idx - 1) // 2):
                return idx

        return -1