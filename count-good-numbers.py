class Solution:
    def countGoodNumbers(self, n: int) -> int:
        def power(x, n):
            if n==0: return 1
            
            res = power(x, n // 2)
            res = res * res
            res = res % mod
            
            return res * x if n % 2 else res

        mod = (10 ** 9) + 7
        four = n // 2
        fo = power(4, four) % mod if n > 1 else 1
        five = (n // 2) + 1 if n % 2 == 1 else n // 2
        fi = power(5, five) % mod
        
        return (fo * fi) % mod
