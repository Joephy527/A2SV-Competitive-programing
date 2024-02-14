class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        minimum = float("inf")
        distribution = [0] * k

        def backTrack(idx):
            nonlocal minimum

            if idx >= len(cookies):
                minimum = min(minimum, max(distribution))
                
                return

            for i in range(len(distribution)):
                if distribution[i] + cookies[idx] < minimum:
                    distribution[i] += cookies[idx]
                    backTrack(idx + 1)
                    distribution[i] -= cookies[idx]

        backTrack(0)

        return minimum
