class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        level = {beginWord}
        word_set = set(wordList)

        if endWord not in word_set:
            return 0

        count = 1

        while level:

            next_level = set()

            for word in level:

                if word == endWord:
                    return count
                
                for i in range(len(word)):
                    for c in "abcdefghijklmnopqrstuvwxyz":

                        if c == word[i]:
                            continue
                        
                        new_word = word[:i] + c + word[i+1:]

                        if new_word in word_set:
                            next_level.add(new_word)

            word_set -= next_level
            count += 1
            level = next_level

        return 0