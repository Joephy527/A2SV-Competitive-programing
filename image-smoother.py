class Solution:
    def imageSmoother(self, img: List[List[int]]) -> List[List[int]]:
        smoothedImg = [[0] * len(img[0]) for _ in range(len(img))]

        for row in range(len(img)):
            for col in range(len(img[0])):
                sumOfCells = numberOfCells = 0

                for i in range(-1, 2):
                    for j in range(-1, 2):
                        r, c = row + i, col + j

                        if r < 0 or r >= len(img) or c < 0 or c >= len(img[0]):
                            continue
            
                        sumOfCells += img[r][c]
                        numberOfCells += 1

                smoothedImg[row][col] = sumOfCells // numberOfCells

        return smoothedImg
