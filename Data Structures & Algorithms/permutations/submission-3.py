class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(cur, visited):
            if len(cur) == len(nums):
                res.append(cur.copy())
                return
            
            for i in range(len(nums)):
                if i in visited:
                    continue # skip number already used in the current path
                
                # make choice
                cur.append(nums[i])
                visited.add(i)

                # recurse
                dfs(cur, visited)

                # undo choices
                visited.remove(i)
                cur.pop()
        
        dfs([], set())
        return res

            
