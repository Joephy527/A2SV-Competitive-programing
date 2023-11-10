class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        res = []
        
        for num in range(left, right + 1):
            check = True

            for i in str(num):
                if i == "0" or num % int(i) != 0:
                    check = False

            if check: res.append(num)

        return res
