class Solution:
    def longestWord(self, words: List[str]) -> str:
        trie = Trie()
        longestWord = ""

        for word in words:
            trie.insert(word)

        for word in words:
            if trie.checkPrefixes(word):
                if len(longestWord) == len(word):
                    longestWord = min(longestWord, word)
                elif len(longestWord) < len(word):
                    longestWord = word

        return longestWord

class Trie:

    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        cur = self.root
        
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            
            cur = cur.children[char]

        cur.isEnd = True

    def checkPrefixes(self, word: str) -> bool:
        cur = self.root

        for char in word:
            cur = cur.children[char]
            if not cur.isEnd:
                return False

        return True

class TrieNode():
    def __init__(self):
        self.isEnd = False
        self.children = {}
