class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = ""
        for string in range(len(strs)):
            strlen = len(strs[string])
            encoded += str(strlen) + "#" +  strs[string]
        return encoded
    def decode(self, s: str) -> List[str]:
        decoded,i = [],0
        
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            decoded.append(s[j+1 : length + j + 1])
            i = j + 1 + length
        return decoded
