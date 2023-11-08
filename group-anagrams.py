class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strsMap = {}

        for i in strs:
            sortI = "".join(sorted(i))

            if sortI not in strsMap:
                strsMap[sortI] = []

            strsMap[sortI].append(i)

        return list(strsMap.values())
