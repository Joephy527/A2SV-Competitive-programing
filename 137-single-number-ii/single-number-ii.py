class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        unique = 0

        for bit_position in range(32):
            bit_count = 0

            for num in nums:
                bit_count += (num >> bit_position) & 1

            if bit_count % 3:
                unique |= 1 << bit_position

        if unique & (1 << 31):
            unique -= 1 << 32

        return unique