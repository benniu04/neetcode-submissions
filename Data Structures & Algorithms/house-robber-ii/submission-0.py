class Solution:
    def rob(self, nums: List[int]) -> int:
        # if there's only one house, just rob it
        if len(nums) == 1:
            return nums[0]
        
        slice_1 = nums[:-1]

        slice_2 = nums[1:]

        return max(self.rob1d(slice_1), self.rob1d(slice_2))

    def rob1d(self, arr: List[int]) -> int:
        mem = {}
        def dfs(i):
            if i >= len(arr):
                return 0
            
            if i in mem:
                return mem[i]
            
            current_house = arr[i] + dfs(i + 2)
            skip_house = dfs(i + 1)

            mem[i] = max(current_house, skip_house)
            return mem[i]
        
        return dfs(0)