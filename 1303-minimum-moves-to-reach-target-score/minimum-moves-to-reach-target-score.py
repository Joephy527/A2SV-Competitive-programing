class Solution:
    def minMoves(self, target: int, maxDoubles: int) -> int:
        moves = 0
        
        while target > 1 and maxDoubles:
            moves += 1 + target % 2
            target //= 2
            maxDoubles -= 1

        return moves + target - 1