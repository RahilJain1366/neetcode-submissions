class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashmap = defaultdict(list)

        for word in strs:
            hashmap[''.join(sorted(word))].append(word)
        
        return list(hashmap.values())