class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        #simpler but slower if you cant remember bucket sorting

        #Counter is a python prebuilt function
        freq = Counter(nums)

        #make sorted items, and 
        sorted_items = sorted(freq.items(), key=lambda x: x[1], reverse=True)

        return [num for num, cnt in sorted_items[:k]]