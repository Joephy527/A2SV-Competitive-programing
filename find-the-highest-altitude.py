class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        s = maxAltitude = 0

        for alt in gain:
            s += alt
            maxAltitude = max(maxAltitude, s)

        return maxAltitude
