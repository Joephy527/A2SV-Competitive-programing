class Solution:
    def sumOfEncryptedInt(self, nums: List[int]) -> int:
        s = 0

        for num in nums:
            strNum = ""
            maxChar = max(str(num))

            for _ in range(len(str(num))):
                strNum += maxChar

            s += int(strNum)

        return s
