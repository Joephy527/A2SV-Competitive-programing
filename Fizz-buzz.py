class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        dic = {3: "Fizz", 5: "Buzz"}
        res = []
        
        for i in range(1, n+1):
            phrase = ""
            for num, word in dic.items():
                if i % num == 0:
                    phrase += word

            res.append(phrase if phrase != "" else str(i))

        return res
