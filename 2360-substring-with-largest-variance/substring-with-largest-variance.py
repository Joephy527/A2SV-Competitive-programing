class Solution:
    def largestVariance(self, s: str) -> int:
        count = Counter(s)
        variance = 0
        
        for a, b in product(set(s), set(s)):
            if a == b: continue

            count_a = count_b = 0
            remains_b = count[b]
            
            for c in s:
                if c == a:
                    count_a += 1
                elif c == b: 
                    count_b += 1
                    remains_b -= 1
                
                if count_b:
                    variance = max(variance, count_a - count_b)
                
                if count_a < count_b and remains_b > 0:
                    count_a, count_b = 0, 0
        
        return variance