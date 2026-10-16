class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        counter_s, counter_t = Counter(s), Counter(t)

        if len(s) != len(t):
            return False
            
        for letter in s:

            if counter_s[letter] != counter_t[letter]:
                return False

        return True