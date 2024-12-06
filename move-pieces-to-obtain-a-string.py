class Solution:
    def canChange(self, start: str, target: str) -> bool:
        length = len(start)
        startIdx = targetIdx = 0

        while startIdx < length or targetIdx < length:
            while startIdx < length and start[startIdx] == "_":
                startIdx += 1

            while targetIdx < length and target[targetIdx] == "_":
                targetIdx += 1

            if startIdx == length or targetIdx == length:
                return startIdx == length and targetIdx == length

            if (start[startIdx] != target[targetIdx] or
                (start[startIdx] == "L" and startIdx < targetIdx) or
                (start[startIdx] == "R" and startIdx > targetIdx)):
                return False

            startIdx += 1
            targetIdx += 1

        return True
