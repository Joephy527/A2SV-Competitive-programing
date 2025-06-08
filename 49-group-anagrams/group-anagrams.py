class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        for s in strs:
            key = sorted(s)
            anagrams[tuple(key)].append(s)

        return list(anagrams.values())