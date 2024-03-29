class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root

        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()

            cur = cur.children[char]

        cur.isEnd = True

    def search(self, word: str) -> bool:
        def dfs(idx, node):
            cur = node

            for i in range(idx, len(word)):
                if word[i] != ".":
                    if word[i] not in cur.children:
                        return False

                    cur = cur.children[word[i]]
                else:
                    for child in cur.children.values():
                        if dfs(i + 1, child):
                            return True

                    return False

            return cur.isEnd

        return dfs(0, self.root)

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEnd = False


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
