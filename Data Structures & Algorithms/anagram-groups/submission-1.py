class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        #make a dictionary
        groups = {}

        for s in strs:
            key = ''.join(sorted(s))
            groups.setdefault(key, []).append(s)
        return list(groups.values())
            
            
