class Solution:
    def escapeGhosts(self, ghosts: List[List[int]], target: List[int]) -> bool:
        myDest = abs(target[1]) + abs(target[0])

        for ghost in ghosts:
            ghostDest = abs(ghost[0] - target[0]) + abs(ghost[1] - target[1])

            if ghostDest <= myDest:
                return False

        return True
