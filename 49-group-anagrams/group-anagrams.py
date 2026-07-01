class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)

        for string in strs:
            count = [0] * 26

            for character in string:
                index = ord(character) - ord("a")
                
                count[index] += 1

            groups[tuple(count)].append(string)

        return list(groups.values())