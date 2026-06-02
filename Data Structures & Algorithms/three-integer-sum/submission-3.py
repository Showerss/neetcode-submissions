class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        

        result = []
        nums.sort()

        for i in range(len(nums)):

            #when sorted, if the smallest number is > 0 then nothing can be done to make anything = 0
            # if nums[i] > 0:
            #     break
            
            left = i+1
            right = len(nums) - 1
            target = -nums[i]

            while left < right:
                sum = nums[left] + nums[right]
                if sum < target:
                    left += 1

                elif sum > target:
                    right -= 1

                else: 
                    triplets = [nums[i], nums[left], nums[right]]
                    if triplets not in result:
                        result.append(triplets)
                    left += 1
                    right -= 1

        return result



