class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        answer = ""
        strs.sort()

        # get shortest word from the first and last word
        smallestWordLength = min(len(strs[0]),len(strs[-1]))
        
        for i in range(smallestWordLength):
            if strs[0][i] != strs[-1][i]:
                return answer
            
            answer += strs[0][i]

        return answer
