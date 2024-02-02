class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        relatedPhrases = {3: "Fizz", 5: "Buzz"}
        result = []

        for number in range(1, n+1):
            phrase = self.getPhrase(relatedPhrases, number)
            result.append(phrase)

        return result

    def getPhrase(self, relatedPhrases, number):
        phrase = ""
        
        for key in relatedPhrases:
            if number % key == 0:
                phrase += relatedPhrases[key]

        return phrase if phrase else str(number)
