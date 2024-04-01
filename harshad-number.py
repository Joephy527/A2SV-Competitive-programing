class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        s = sum([int(digit) for digit in str(x)])
        res = -1

        if not x % s:
            res = s
        
        return res 
