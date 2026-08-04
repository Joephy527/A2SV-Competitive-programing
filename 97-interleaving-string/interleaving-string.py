class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n, m = len(s1), len(s2)
        
        if n + m != len(s3):
            return False
        
        memo = {(n, m): True}

        def dfs(p1, p2):
            if (p1, p2) not in memo:
                p3 = p1 + p2

                take_s1 = (
                    p1 < n and
                    s1[p1] == s3[p3] and
                    dfs(p1 + 1, p2)
                )

                take_s2 = (
                    p2 < m and
                    s2[p2] == s3[p3] and
                    dfs(p1, p2 + 1)
                )

                memo[(p1, p2)] = take_s1 or take_s2

            return memo[(p1, p2)]

        return dfs(0, 0)