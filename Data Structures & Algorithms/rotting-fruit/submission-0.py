class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])
        visited = set()
        q = collections.deque()
        fresh = 0

        def addMin(r, c):
            nonlocal fresh
            if (r < 0 or r == ROW or c < 0 or
                c == COL or (r, c) in visited or grid[r][c] != 1):
                return
            
            q.append((r, c))
            visited.add((r, c))
            fresh -= 1

        for r in range(ROW):
            for c in range(COL):
                if grid[r][c] == 2:
                    q.append((r, c))
                    visited.add((r, c))
                elif grid[r][c] == 1:
                    fresh += 1
        
        if fresh == 0:
            return 0
        
        min_mins = 0
        while q and fresh > 0:
            for i in range(len(q)):
                r, c = q.popleft()

                addMin(r + 1, c)
                addMin(r - 1, c)
                addMin(r, c + 1)
                addMin(r, c - 1)


            min_mins += 1
        
        return min_mins if fresh == 0 else -1