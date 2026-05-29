class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        #this creates a dict with default keys
        groups = defaultdict(list)

        for s in strs: #for each string in strs, label it s
            key = ''.join(sorted(s)) #replace the default key as the sorted
            groups[key].append(s)

        return list(groups.values()) #print the values

            

            

