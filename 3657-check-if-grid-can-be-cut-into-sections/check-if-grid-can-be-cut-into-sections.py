class Solution:
    def checkValidCuts(self, n: int, rectangles: List[List[int]]) -> bool:
        def check_cuts(idx):
            rectangles.sort(key=lambda x: x[idx])
            max_end = rectangles[0][idx + 2]
            cuts = 0

            for i in range(1, len(rectangles)):
                

                if rectangles[i][idx] >= max_end:
                    cuts += 1 

                max_end = max(max_end, rectangles[i][idx + 2])

            return cuts > 1

        return (
            check_cuts(0) or check_cuts(1)
        )