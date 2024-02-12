class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        leftCount = leftCost = rightCount = rightCost = 0
        length  = len(boxes)
        numberOfMoves = [0] * length


        for i in range(1, length):
            if boxes[i-1] == "1":
                leftCount += 1

            leftCost += leftCount
            numberOfMoves[i] += leftCost

        for i in range(length-2, -1, -1):
            if boxes[i+1] == "1":
                rightCount += 1

            rightCost += rightCount
            numberOfMoves[i] += rightCost

        return numberOfMoves
