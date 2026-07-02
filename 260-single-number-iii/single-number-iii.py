class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        combined = 0

        for num in nums:
            combined ^= num

        set_bit = combined & -combined
        first_num = second_num = 0

        for num in nums:
            if set_bit & num:
                first_num ^= num
            else:
                second_num ^= num

        return [first_num, second_num]