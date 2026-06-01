class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        #simpler but slower if you cant remember bucket sorting

        #Counter is a python prebuilt function you can use instead of doing a dictionary and doing count[n] = 1 + count.get(n, 0)
        freq = Counter(nums)
        #basically after here, freq is a dictionary now

        #every dictionary has a .items() functions that returns a list of (key, value) pairs
        sorted_items = sorted(freq.items(), 
                                key=lambda x: x[1], #sort by the count
                                reverse=True) #this makes it descending

        return [num for num, cnt in sorted_items[:k]] #pick the first k numbers