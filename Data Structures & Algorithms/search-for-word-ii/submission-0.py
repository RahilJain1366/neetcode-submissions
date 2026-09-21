class TrieNode:

    def __init__(self):
        self.children = {}
        self.isEnd = False
    
class Trie:

    def __init__(self):

        self.root = TrieNode()
    
    def _insert(self, word):

        node = self.root

        for letter in word:

            if letter not in node.children:
                node.children[letter] = TrieNode()
            
            node = node.children[letter]
        
        node.isEnd = True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        
        rows, cols = len(board), len(board[0])

        trie = Trie()
        for word in words:
            trie._insert(word)

        res, visited = set(), set()

        def backtrack(row, col, node, word):

            if row < 0 or row >= rows or col < 0 or col >= cols or board[row][col] not in node.children or (row, col) in visited:
                return 
            
            visited.add((row, col))
            node = node.children[board[row][col]]
            word += board[row][col]

            for dr, dc in [(0,1),(1,0),(0,-1),(-1,0)]:
                backtrack(row + dr, col + dc, node, word)
            
            if node.isEnd:
                res.add(word)

            visited.remove((row, col))

        for row in range(rows):
            for col in range(cols):

                backtrack(row, col, trie.root, "")

        return list(res)
        