class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
        prefix = odd = even = odd_sum = 0
        mod = (10 ** 9) + 7

        for num in arr:
            prefix += num

            if prefix % 2:
                odd_sum = (odd_sum + 1 + even) % mod
                odd += 1
            else:
                odd_sum = (odd_sum + odd) % mod
                even += 1

        return odd_sum
