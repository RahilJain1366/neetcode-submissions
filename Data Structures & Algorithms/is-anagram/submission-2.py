class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        hashmaps, hashmapt = {}, {}

        if len(s) != len(t):
            return False

        for i in range(len(s)):
            hashmaps[s[i]] = 1 + hashmaps.get(s[i],0)
            hashmapt[t[i]] = 1 + hashmapt.get(t[i], 0)

        for c in hashmaps:
            if hashmaps[c] != hashmapt.get(c,0):
                return False
        return True
       

        