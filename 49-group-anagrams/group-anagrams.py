class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)

        def get_key(string):
            count = [0] * 26

            for char in string:
                count[ord(char) - ord("a")] += 1

            return tuple(count)

        for s in strs:
            key = get_key(s)

            anagrams[key].append(s)

        return list(anagrams.values())