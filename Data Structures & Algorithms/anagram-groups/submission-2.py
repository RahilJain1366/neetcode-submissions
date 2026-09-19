class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashmap_sorted = defaultdict(list)
        for word in strs:
            hashmap_sorted[''.join(sorted(word))].append(word)

        #print(list(hashmap_sorted.values()))
        return list(hashmap_sorted.values())
        

