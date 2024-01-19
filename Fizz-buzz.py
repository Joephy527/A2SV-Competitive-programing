class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        dic = {3: "Fizz", 5: "Buzz"}
        res = []
        
        for i in range(1, n+1):
            phrase = ""
            for key in dic:
                if i % key == 0:
                    phrase += dic[key]

            res.append(phrase if phrase != "" else str(i))

        return res
