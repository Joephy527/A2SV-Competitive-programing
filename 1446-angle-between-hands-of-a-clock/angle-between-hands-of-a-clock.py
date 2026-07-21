class Solution:
    def angleClock(self, hour: int, minutes: int) -> float:
        hour %= 12
        hour += minutes / 60
        minutes /= 5

        one_side = abs(hour - minutes) * 30

        return min(one_side, 360 - one_side)