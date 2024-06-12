class Solution:
    def isAdditiveNumber(self, num: str) -> bool:
        def backTrack(idx, first, second):
            if idx == len(num):
                return True

            if second or second == 0:
                for i in range(idx, len(num)):
                    newCur = num[idx:i + 1]

                    if len(newCur) > 1 and newCur[0] == "0":
                        continue

                    if int(newCur) == first + second:
                        if backTrack(i + 1, second, int(newCur)):
                            return True
            else:
                for i in range(idx, len(num) - 1):
                    newSecond = num[idx:i + 1]
                    
                    if len(newSecond) > 1 and newSecond[0] == "0":
                        continue

                    if backTrack(i + 1, first, int(newSecond)):
                        return True

        for i in range(len(num) - 2):
            newNum = num[:i + 1]

            if len(newNum) > 1 and newNum[0] == "0":
                continue
            
            if backTrack(i + 1, int(newNum), ""):
                return True
