class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        hashmap = {}
        left = 0
        n = len(s)
        res = 0

        for right in range(n):

            if s[right] in hashmap:
                left = max(hashmap[s[right]], left)
            
            hashmap[s[right]] = right + 1
            res = max(res, right - left + 1)

        return res
