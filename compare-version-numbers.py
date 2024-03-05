class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        listV1 = list(map(int, version1.split(".")))
        listV2 = list(map(int, version2.split(".")))

        for i in range(max(len(listV1), len(listV2))):
            v1 = listV1[i] if i < len(listV1) else 0
            v2 = listV2[i] if i < len(listV2) else 0

            if v1 < v2: return -1
            
            if v1 > v2: return 1

        return 0
