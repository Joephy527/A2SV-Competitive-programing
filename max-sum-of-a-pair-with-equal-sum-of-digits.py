class Solution:
    def maximumSum(self, nums: List[int]) -> int:
        digit_sum = [0] * 82
        max_pair = -1

        def get_digit_sum(num):
            digit_sum = 0

            while num > 0:
                digit_sum += num % 10
                num //= 10

            return digit_sum

        for num in nums:
            cur_digit_sum = get_digit_sum(num)

            num_i = digit_sum[cur_digit_sum]

            if num_i:
                max_pair = max(max_pair, num_i + num)

            digit_sum[cur_digit_sum] = max(num_i, num)

        return max_pair
