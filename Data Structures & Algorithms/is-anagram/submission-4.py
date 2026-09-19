class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        counter_s = collections.Counter(s)
        counter_t = collections.Counter(t)

        return counter_s == counter_t