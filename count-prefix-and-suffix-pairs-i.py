class TrieNode:
    def __init__(self):
        self.children = {}
        self.count = 0

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        node = self.root

        for first_char, last_char in zip(word, reversed(word)):
            if (first_char, last_char) not in node.children:
                node.children[(first_char, last_char)] = TrieNode()

            node = node.children[(first_char, last_char)]
            node.count += 1

        return node.count - 1

class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        trie = Trie()
        pairs = 0

        for word in reversed(words):
            pairs += trie.add(word)

        return pairs
