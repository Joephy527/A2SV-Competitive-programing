class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        digitStr = "".join([str(digit) for digit in digits])
        incrementNumStr = str(int(digitStr) + 1)
        finalDigits = [int(num) for num in incrementNumStr]

        return finalDigits
