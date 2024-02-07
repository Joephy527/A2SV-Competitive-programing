class Solution:
    def longestWord(self, words: List[str]) -> str:
        words.sort()
        trie = Trie()
        longestWord = ""

        for word in words:
            lastNode = trie.insert(word)

            if (lastNode.val == len(word) and
                lastNode.val > len(longestWord)):
                longestWord = word

        return longestWord


class Trie:

    def __init__(self):
        self.root = TrieNode(0)

    def insert(self, word: str) -> None:
        cur = self.root
        count = 0
        
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode(count)
            
            cur = cur.children[char]

            if cur.isEnd: count += 1

        cur.isEnd = True
        cur.val += 1

        return cur

class TrieNode():
    def __init__(self, val):
        self.isEnd = False
        self.children = {}
        self.val = val
