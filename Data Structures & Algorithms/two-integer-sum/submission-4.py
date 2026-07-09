class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_to_find = {}

        for i, num in enumerate(nums):
            complement = target - num
            if complement in nums_to_find:
                return [nums_to_find[complement], i]
            nums_to_find[num] = i
        
        return []

        