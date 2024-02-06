class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        trie = Trie()
        for word in strs:
            trie.insert(word)
        
        return trie.longestPrefix()

class TrieNode:

    def __init__(self):
        self.children = {}
        self.isWord = False
    
class Trie:
    
    def __init__(self):
        self.root = TrieNode()
        
    def insert(self, word):
        cur = self.root

        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()

            cur = cur.children[char]

        cur.isWord = True
            
    def longestPrefix(self):
        cur = self.root
        longest = ""

        while cur and len(cur.children) == 1 and not cur.isWord:
            longest += list(cur.children)[0]
            cur = cur.children[list(cur.children)[0]]
        
        return longest
