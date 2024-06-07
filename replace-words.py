class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        trie = Trie()
        res = []
        
        for word in dictionary:
            trie.insert(word)

        for derivative in sentence.split():
            res.append(trie.search(derivative))

        return " ".join(res)

class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, word):
        cur = self.root
        
        for c in word:
            if c not in cur:
                cur[c] = {}

            cur = cur[c]

        cur["#"] = True

    def search(self, word):
        res = []
        cur = self.root

        for c in word:
            if c not in cur:
                return word

            cur = cur[c]
            res.append(c)

            if "#" in cur:
                return "".join(res)
        
        return word
