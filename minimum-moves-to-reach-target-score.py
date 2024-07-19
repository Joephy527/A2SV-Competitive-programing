class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        odds = doubles = 0
        
        for _ in range(maxDoubles):
            if target == 1: break

            odds += target % 2
            target //= 2
            doubles += 1

        return target - 1 + doubles + odds
