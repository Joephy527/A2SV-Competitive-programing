class Solution:
    def countPrimes(self, n: int) -> int:
        if n < 3: return 0

        check = [1] * n
        check[0] = check[1] = 0
        m = 2

        while m ** 2 < n:
            if check[m] == 1:
                for i in range(m ** 2, n, m):
                    check[i] = 0

            m += 1 if m == 2 else 2

        return sum(check)
