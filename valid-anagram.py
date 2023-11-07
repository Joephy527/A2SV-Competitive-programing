class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS = Counter(s)
        countT = Counter(t)

        return countT == countS
        
