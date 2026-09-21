class TrieNode:
    
    def __init__(self):
        self.children = {}
        self.isEnd = False

class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        node = self.root

        for letter in word:

            if letter not in node.children:
                node.children[letter] = TrieNode()
            node = node.children[letter]
        
        node.isEnd = True
    

    def search(self, word: str) -> bool:
        
        def dfs(node, index):

            if index == len(word):
                return node.isEnd
            
            letter = word[index]

            if letter != ".":
                if letter not in node.children:
                    return False
                
                return dfs(node.children[letter], index + 1)
            
            for child in node.children.values():
                if dfs(child, index + 1):
                    return True
                
            return False
        
        return dfs(self.root, 0)


