class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # use a map
        preMap = {}

        for i, n in enumerate(nums):
            diff = target - n
            if diff in preMap:
                return [preMap[diff], i]
            preMap[n] = i


        