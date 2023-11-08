class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strsMap = defaultdict(list)

        for i in strs:
            sortI = "".join(sorted(i))
            strsMap[sortI].append(i)

        return strsMap.values()
