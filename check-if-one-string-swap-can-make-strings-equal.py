class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        idx1 = idx2 = swaps = 0

        for i in range(len(s1)):
            if s1[i] != s2[i]:
                swaps += 1

                if swaps > 2:
                    return False
                elif swaps == 1:
                    idx1 = i
                else:
                    idx2 = i

        return (
            s1[idx1] == s2[idx2] and
            s1[idx2] == s2[idx1]
        )
