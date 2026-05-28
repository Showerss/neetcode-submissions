class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        listOfNums = []

        for i in nums:
            if i in listOfNums:
                return True
            listOfNums.append(i)
        
        return False