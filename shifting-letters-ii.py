class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        d = [0 for _ in range(n + 1)]
        
        for shift in shifts:
            di = 1 if shift[2] else -1
            d[shift[0]] += di
            d[shift[1] + 1] -= di
        
        res = []
        for i in range(n):
            if i != 0: 
                d[i] += d[i - 1]
            
            newChr = (ord(s[i]) - ord("a") + d[i]) % 26 + ord("a")
            res.append(chr(newChr))
        return "".join(res)
