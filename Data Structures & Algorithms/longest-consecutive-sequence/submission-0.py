class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        nums_set = set(nums)
        count = 0

        for num in nums_set:
            if (num - 1) not in nums_set:
                length = 1

                while (num + length) in nums_set:
                    length += 1
                count = max(length, count)
        
        return count