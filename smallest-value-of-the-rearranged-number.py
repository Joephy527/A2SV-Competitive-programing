class Solution:
    def smallestNumber(self, num: int) -> int:
        if num < 10 and num > -1:
            return num
        
        strNum = list(str(num))
        if num > 0:
            strNum.sort()
            if strNum[0] == "0":
                for i in range(len(strNum)):
                    if strNum[i] != "0":
                        strNum[0], strNum[i] = strNum[i], strNum[0]
                        break

            return int("".join(strNum))
        else:
            sortedNum = strNum[1:]
            sortedNum.sort(reverse=True)
            
            return int("-" + "".join(sortedNum))
