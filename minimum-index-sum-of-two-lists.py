class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        list2Map = {s: idx for idx, s in enumerate(list2)}
        leastIdxStr, leastIdxSum = [], float("inf")

        for idx, s in enumerate(list1):
            if s in list2Map:
                sumIdx = idx + list2Map[s]

                if leastIdxSum == sumIdx:
                    leastIdxStr.append(s)
                elif leastIdxSum > sumIdx:
                    leastIdxStr = [s]
                    leastIdxSum = sumIdx

        return leastIdxStr
