class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False

class Trie:
    def __init__(self):
        self.node = TrieNode()

    def add_word(self, word):
        cur = self.node

        for c in word:
            if c not in cur.children:
                cur.children[c] = TrieNode()

            cur = cur.children[c]

        cur.is_word = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        rows, cols = len(board), len(board[0])
        directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
        visited = [[False] * cols for _ in range(rows)]
        words_on_board = []

        trie = Trie()

        for word in words:
            trie.add_word(word)

        def is_inbounds(row, col):
            return rows > row >= 0 <= col < cols

        def back_track(row, col, node, word):
            if (
                not is_inbounds(row, col) or
                visited[row][col] or
                board[row][col] not in node.children
            ):
                return

            char = board[row][col]
            word.append(char)
            visited[row][col] = True
            node = node.children[char]

            if node.is_word:
                node.is_word = False
                words_on_board.append("".join(word))

            for x, y in directions:
                r, c = row + x, col + y
                back_track(r, c, node, word)

            visited[row][col] = False
            word.pop()

        for r in range(rows):
            for c in range(cols):
                back_track(r, c, trie.node, [])

        return words_on_board
