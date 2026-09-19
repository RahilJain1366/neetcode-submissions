class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        hashmap_s = collections.Counter(s)
        hashmap_t = collections.Counter(t)

        for val in s:
            if hashmap_s[val] != hashmap_t[val]:
                return False

        return True


        
        

        