class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        def removePairs(pair, s, point):
            stack = []
            pairPoints = 0

            for c in s:
                if c == pair[1] and stack and stack[-1] == pair[0]:
                    stack.pop()
                    pairPoints += point
                else:
                    stack.append(c)

            s = "".join(stack)

            return pairPoints, s

        maxPoints = 0
        pair = "ab" if x > y else "ba"
        
        maxPoint, s = removePairs(pair, s, max(x, y))
        maxPoints += maxPoint
        maxPoints += removePairs(pair[::-1], s, min(x, y))[0]

        return maxPoints
