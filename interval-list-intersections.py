class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        intersection = []
        p1 = p2 = 0

        while p1 < len(firstList) and p2 < len(secondList):
            leftI, rightI = firstList[p1]
            leftJ, rightJ = secondList[p2]

            left = max(leftI, leftJ)
            right = min(rightI, rightJ)

            if left <= right:
                intersection.append([left, right])

            if rightI <= rightJ:
                p1 += 1
            else:
                p2 += 1

        return intersection
