class Solution:
    def romanToInt(self, s: str) -> int:
        romanToNumeralMap = {
            "I": 1,        
            "V": 5,        
            "X": 10,        
            "L": 50,        
            "C": 100,        
            "D": 500,        
            "M": 1000,        
        }
        integer = 0

        for i in range(len(s) - 1):
            if romanToNumeralMap[s[i]] < romanToNumeralMap[s[(i+1)]]:
                integer -= romanToNumeralMap[s[i]]
            else:
                integer += romanToNumeralMap[s[i]]

        return integer + romanToNumeralMap[s[-1]]
