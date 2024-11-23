class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        rows, cols = len(box), len(box[0])
        rotatedBox = []

        for r in range(rows):
            swapIdx = cols - 1

            for c in reversed(range(cols)):
                if box[r][c] == "#":
                    box[r][c], box[r][swapIdx] = box[r][swapIdx], box[r][c]
                    swapIdx -= 1

                if box[r][c] == "*":
                    swapIdx = c - 1

        for c in range(cols):
            reversedRow = []
            
            for r in reversed(range(rows)):
                reversedRow.append(box[r][c])

            rotatedBox.append(reversedRow)

        return rotatedBox
