class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = 0
        hashmap = {}
        res = 0
        for r in range(len(s)):
            hashmap[s[r]] = 1 + hashmap.get(s[r],0)
            res = max(res,hashmap[s[r]])

            if (r - l + 1) - res > k:
                hashmap[s[l]] -= 1
                l += 1
        return (r-l+1)




        