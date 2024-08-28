from collections import deque
class Solution:
    def hasValidPath(self, grid: List[List[int]]) -> bool:
        rows, cols =  len(grid), len(grid[0])
        queue = deque([(0,0)])
        visited = set()
        directions = {
            1: [(0, -1), (0, 1)],
            2: [(-1, 0), (1, 0)],
            3: [(0, -1), (1, 0)],
            4: [(0, 1), (1, 0)],
            5: [(0, -1), (-1, 0)],
            6: [(0, 1), (-1, 0)]
        }

        def validPath(row,col): 
            return row < rows and row >= 0 and col < cols and col >= 0 and (row,col) not in visited
        
    
        
        while queue:
            row, col = queue.pop()
            
            if row == rows - 1 and col == cols - 1:
                return True

            visited.add((row,col))
            cell = grid[row][col]

            for r, c in directions[cell]:
                newR, newC = row + r, col + c
                
                if validPath(newR,newC):
                    newCell = grid[newR][newC]
                    if (-r,-c) in directions[newCell]:
                        queue.append((newR, newC))

        return
