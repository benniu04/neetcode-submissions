class Solution:
    def rob(self, nums: List[int]) -> int:
        mem = {}

        def dfs(i):
            if i >= len(nums):
                return 0
            
            if i in mem:
                return mem[i]
            
            # compute current_rob and skip_rob
            current_rob = nums[i] + dfs(i + 2)
            skip_rob = dfs(i + 1)

            mem[i] = max(current_rob, skip_rob)
            return mem[i]
        
        return dfs(0)
            
            
        
