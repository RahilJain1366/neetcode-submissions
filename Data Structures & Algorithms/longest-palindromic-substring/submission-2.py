class Solution:
    def longestPalindrome(self, s: str) -> str:

        resId = 0
        resLen = 0

        if len(s) == 1:
            return s

        for k in range(len(s)):
            i, j = k, k 
            while i >= 0 and j < len(s) and s[i] == s[j]:
                if (j-i + 1) > resLen:
                    resIdx = i
                    resLen = j - i + 1
                i -= 1
                j += 1

            i, j = k, k + 1

            while i >= 0 and j < len(s) and s[i] == s[j]:
                if (j - i + 1) > resLen:
                    resIdx = i
                    resLen = j - i + 1
                i -= 1
                j += 1

        return s[resIdx : resIdx + resLen]

