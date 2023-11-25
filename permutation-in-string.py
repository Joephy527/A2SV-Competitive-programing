class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2): return False

        countS1 = Counter(s1)
        countS2 = Counter(s2[:len(s1) - 1])
        l, r = 0, len(s1) - 1

        while r < len(s2):
            countS2[s2[r]] += 1

            if countS1 == countS2:
                return True

            countS2[s2[l]] -= 1
            l += 1
            r += 1
